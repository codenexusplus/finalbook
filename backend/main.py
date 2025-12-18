import os
import argparse
import logging
import cohere
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
from urllib.parse import urlparse, urljoin
import uuid
import xml.etree.ElementTree as ET

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

if not all([COHERE_API_KEY, QDRANT_URL, QDRANT_API_KEY]):
    logging.error("Missing one or more environment variables: COHERE_API_KEY, QDRANT_URL, QDRANT_API_KEY")
    exit(1)

# Initialize clients
cohere_client = cohere.Client(COHERE_API_KEY)
qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

def create_qdrant_collection(collection_name: str):
    """Creates the Qdrant collection if it does not already exist."""
    try:
        if not qdrant_client.collection_exists(collection_name=collection_name):
            qdrant_client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE),
            )
            logging.info(f"Collection '{collection_name}' created successfully.")
        else:
            logging.info(f"Collection '{collection_name}' already exists. Skipping creation.")
    except Exception as e:
        logging.error(f"Failed to create collection '{collection_name}': {e}")
        raise

def get_urls_from_sitemap(sitemap_url: str) -> list[str]:
    """Fetches a sitemap and extracts all URLs, replacing localhost."""
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
        
        root = ET.fromstring(response.content)
        urls = []
        for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
            url = elem.text
            if url:
                # Replace localhost with the actual live site URL
                if "localhost:3000" in url:
                    url = url.replace("https://localhost:3000", "https://finalbook-ss4z.vercel.app")
                urls.append(url)
        return urls
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch sitemap: {e}")
        return []
    except ET.ParseError as e:
        logging.error(f"Failed to parse sitemap XML: {e}")
        return []

def extract_text_from_url(url: str) -> str:
    """Fetches HTML from a URL and extracts clean text, preserving code blocks."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove header, footer, nav, and sidebar elements
        for selector in ["header", "footer", "nav", "aside", ".navbar", ".sidebar", ".table-of-contents"]:
            for element in soup.select(selector):
                element.extract()

        # Remove script and style elements
        for script_or_style in soup(["script", "style"]):
            script_or_style.extract()

        # Try to find the main content area with known Docusaurus IDs/classes
        main_content = None
        if not main_content:
            main_content = soup.find(id='docusaurus_skipToContent_fallback') # Common Docusaurus ID
        if not main_content:
            main_content = soup.find('div', class_='theme-doc-markdown markdown') # Combined class
        if not main_content:
            main_content = soup.find('article', class_='markdown') # Fallback to article.markdown
        if not main_content:
            main_content = soup.find('div', class_='col') # Fallback to a common content column
        if not main_content:
            main_content = soup.find('main', role='main') # Generic main content tag
        if not main_content:
            main_content = soup.find('div', class_='main-wrapper') # Another common wrapper
        if not main_content:
            main_content = soup.find('div', class_='docItemCol') # Specific Docusaurus docs column
        if not main_content:
            main_content = soup.body # Ultimate fallback

        if not main_content:
            logging.warning(f"Could not identify main content for {url}. Returning empty.")
            return ""

        text_parts = []
        # Extract text from p, h1-h6, li, code, pre, and also directly from the main_content if it's a generic div/body
        for tag in main_content.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'code', 'pre', 'div']):
            if tag.name == 'pre': # Preserve preformatted text (code blocks)
                text_parts.append(tag.get_text(separator="\n", strip=True))
            else:
                # Get text from other tags, ensure it's not empty after stripping
                content = tag.get_text(strip=True)
                if content:
                    text_parts.append(content)
        
        return "\n\n".join(text_parts)

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve or parse {url}: {e}")
        return ""
    except Exception as e:
        logging.error(f"Error extracting text from {url}: {e}")
        return ""

def chunk_text(text: str, max_chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """Splits text into chunks of a maximum size with optional overlap."""
    if not text:
        return []

    chunks = []
    current_chunk = []
    current_length = 0

    sentences = text.split('.') # Simple sentence splitting

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        
        # Estimate token count; a simple character count is often sufficient for basic chunking
        # For a more accurate count, one might use a tokenizer specific to the embedding model
        sentence_length = len(sentence.split()) # Rough word count

        if current_length + sentence_length + len(current_chunk) > max_chunk_size:
            if current_chunk:
                chunks.append(". ".join(current_chunk) + ".")
                
                # Apply overlap by taking the last 'overlap' words
                overlap_text = ". ".join(current_chunk[-overlap:])
                current_chunk = [overlap_text.strip()] if overlap_text.strip() else []
                current_length = len(current_chunk[0].split()) if current_chunk else 0
            
            # If a single sentence is too long, it will form its own chunk
            if sentence_length > max_chunk_size:
                chunks.append(sentence + ".")
                current_chunk = []
                current_length = 0
                continue


        current_chunk.append(sentence)
        current_length += sentence_length + 1 # +1 for the space/separator

    if current_chunk:
        chunks.append(". ".join(current_chunk) + ".")

    return [chunk.strip() for chunk in chunks if chunk.strip()]

def embed_chunks(chunks: list[str]) -> list[list[float]]:
    """Generates embeddings for a list of text chunks using the Cohere client."""
    if not chunks:
        return []
    try:
        response = cohere_client.embed(
            texts=chunks,
            model='embed-english-v3.0',
            input_type='search_document'
        )
        return response.embeddings
    except Exception as e:
        logging.error(f"Failed to generate embeddings: {e}")
        return []

def save_chunks_to_qdrant(collection_name: str, chunks: list[str], vectors: list[list[float]], source_url: str):
    """Saves text chunks and their embeddings to Qdrant."""
    if not chunks or not vectors:
        logging.warning("No chunks or vectors to save to Qdrant.")
        return

    points = []
    for i, (chunk, vector) in enumerate(zip(chunks, vectors)):
        # Generate a unique ID for each point
        point_id = str(uuid.uuid4())
        points.append(
            models.PointStruct(
                id=point_id,
                vector=vector,
                payload={
                    "text": chunk,
                    "source": source_url,
                    "chunk_id": i  # Sequential index within the source document
                },
            )
        )
    try:
        operation_info = qdrant_client.upsert(
            collection_name=collection_name,
            wait=True,
            points=points,
        )
        logging.info(f"Successfully saved {len(points)} points to Qdrant. Status: {operation_info.status}")
    except Exception as e:
        logging.error(f"Failed to save points to Qdrant: {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description="Ingest documentation from a Docusaurus site into Qdrant.")
    parser.add_argument("--sitemap-url", type=str, required=True, help="The URL of the sitemap.xml file.")
    parser.add_argument("--collection-name", type=str, default="rag_embedding", help="The name of the Qdrant collection to use.")
    args = parser.parse_args()

    # Create/recreate Qdrant collection
    create_qdrant_collection(args.collection_name)

    # Get all URLs from sitemap
    logging.info(f"Fetching URLs from sitemap: {args.sitemap_url}")
    urls = get_urls_from_sitemap(args.sitemap_url)
    logging.info(f"Found {len(urls)} URLs to process.")

    for url in urls:
        logging.info(f"Processing URL: {url}")
        text = extract_text_from_url(url)
        if text:
            chunks = chunk_text(text)
            if chunks:
                vectors = embed_chunks(chunks)
                if vectors:
                    save_chunks_to_qdrant(args.collection_name, chunks, vectors, url)
                else:
                    logging.warning(f"No embeddings generated for URL: {url}")
            else:
                logging.warning(f"No chunks generated for URL: {url}")
        else:
            logging.warning(f"No text extracted from URL: {url}")

    logging.info("Ingestion pipeline finished.")


if __name__ == "__main__":
    main()