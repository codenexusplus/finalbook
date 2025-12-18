import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import cohere
import psycopg2
from qdrant_client import QdrantClient, models
from vector_db import get_qdrant_client, COLLECTION_NAME, VECTOR_DIMENSION

load_dotenv()

# --- Configuration ---
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
DATABASE_URL = os.getenv("NEON_DATABASE_URL")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
VERCEL_URL = os.getenv("VERCEL_URL", "https://your-vercel-site.vercel.app")  # Add this to your .env
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150


def extract_text_from_html(html_content, url):
    """Extract text content from HTML"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()
    
    # Get text and clean it up
    text = soup.get_text()
    
    # Clean up the text by removing extra whitespace
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = ' '.join(chunk for chunk in chunks if chunk)
    
    # Create a document-like object with metadata
    class Document:
        def __init__(self, page_content, metadata):
            self.page_content = page_content
            self.metadata = metadata
    
    return Document(page_content=text, metadata={"source": url})


def get_sitemap_urls(sitemap_url, base_domain=None):
    """Extract URLs from a sitemap.xml file"""
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'xml')  # Use xml parser for sitemaps
        urls = []

        # Look for <url><loc> elements in the sitemap
        for url_element in soup.find_all('loc'):
            url = url_element.text.strip()

            # If base_domain is provided and URL contains localhost, replace with actual domain
            if base_domain and "localhost" in url:
                # Replace localhost:3000 with the actual domain
                url = url.replace("localhost:3000", base_domain.replace("https://", "").replace("http://", ""))
            elif base_domain and "127.0.0.1" in url:
                # Also handle 127.0.0.1
                url = url.replace("127.0.0.1:3000", base_domain.replace("https://", "").replace("http://", ""))

            urls.append(url)

        # Also look for sitemaps within sitemaps (sitemap index)
        for sitemap_element in soup.find_all('sitemap'):
            loc = sitemap_element.find('loc')
            if loc:
                sub_sitemap_url = loc.text.strip()

                # Update sub-sitemap URL if localhost is present
                if base_domain and "localhost" in sub_sitemap_url:
                    sub_sitemap_url = sub_sitemap_url.replace("localhost:3000", base_domain.replace("https://", "").replace("http://", ""))

                print(f"Found sub-sitemap: {sub_sitemap_url}")
                # Recursively get URLs from sub-sitemaps
                sub_urls = get_sitemap_urls(sub_sitemap_url, base_domain)
                urls.extend(sub_urls)

        return urls
    except Exception as e:
        print(f"Error parsing sitemap {sitemap_url}: {e}")
        return []


def get_all_pages_from_vercel(base_url):
    """Scrapes all accessible pages from a Vercel website using sitemap.xml if available"""
    # First, try to get URLs from sitemap.xml
    sitemap_url = f"{base_url}/sitemap.xml"
    print(f"Attempting to load sitemap from: {sitemap_url}")

    urls = get_sitemap_urls(sitemap_url, base_url)

    if not urls:
        print("No URLs found in sitemap, using web scraping approach...")
        # Fallback to web scraping if no sitemap
        visited_urls = set()
        urls_to_visit = [base_url]
        documents = []

        while urls_to_visit and len(visited_urls) < 50:  # Limit to prevent infinite crawling
            current_url = urls_to_visit.pop(0)

            if current_url in visited_urls or not current_url.startswith(base_url):
                continue

            visited_urls.add(current_url)
            print(f"Scraping: {current_url}")

            try:
                response = requests.get(current_url, timeout=10)
                response.raise_for_status()

                # Extract text from the page
                document = extract_text_from_html(response.text, current_url)
                documents.append(document)

                # Find all links on the page
                soup = BeautifulSoup(response.text, 'html.parser')
                for link in soup.find_all('a', href=True):
                    href = link['href']

                    # Convert relative URLs to absolute URLs
                    absolute_url = urljoin(current_url, href)

                    # Only add URLs from the same domain and not already visited
                    if (urlparse(absolute_url).netloc == urlparse(base_url).netloc
                        and absolute_url not in visited_urls
                        and not absolute_url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.pdf', '.zip'))):  # Skip media files
                        urls_to_visit.append(absolute_url)

            except Exception as e:
                print(f"Error scraping {current_url}: {e}")
                continue
    else:
        print(f"Found {len(urls)} URLs from sitemap, processing them...")
        documents = []
        for url in urls:
            print(f"Processing from sitemap: {url}")
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()

                # Extract text from the page
                document = extract_text_from_html(response.text, url)
                documents.append(document)
            except Exception as e:
                print(f"Error processing {url}: {e}")
                continue

    return documents


def main():
    """
    Main function to ingest data from a Vercel URL into the vector database.
    """
    # 1. Load documents from Vercel URL
    print(f"Loading documents from {VERCEL_URL}...")
    documents = get_all_pages_from_vercel(VERCEL_URL)
    print(f"Loaded {len(documents)} documents.")

    # 2. Split documents into chunks
    print("Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks.")

    # 3. Initialize clients
    co = cohere.Client(COHERE_API_KEY)
    
    if DATABASE_URL:
        db_conn = psycopg2.connect(DATABASE_URL)
    else:
        db_conn = None
        
    qdrant_client = get_qdrant_client()

    # 4. Create Qdrant collection if it doesn't exist
    try:
        collections = qdrant_client.get_collections().collections
        if COLLECTION_NAME not in [c.name for c in collections]:
            qdrant_client.recreate_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=models.VectorParams(size=VECTOR_DIMENSION, distance=models.Distance.COSINE),
            )
            print(f"Collection '{COLLECTION_NAME}' created.")
        else:
            print(f"Collection '{COLLECTION_NAME}' already exists.")
    except Exception as e:
        print(f"Error creating collection: {e}")
        return

    # 5. Ingest chunks
    print("Ingesting chunks into vector store...")
    batch_size = 100
    for i in range(0, len(chunks), batch_size):
        batch_chunks = chunks[i:i + batch_size]
        texts = [chunk.page_content for chunk in batch_chunks]

        # Get embeddings from Cohere
        embeds = co.embed(texts=texts, model='embed-english-v3.0', input_type='search_document').embeddings

        # Insert into Qdrant only (no PostgreSQL dependency required)
        for chunk, vector in zip(batch_chunks, embeds):
            point_id = hash(chunk.page_content) % 1000000  # Simple ID generation
            qdrant_client.upsert(
                collection_name=COLLECTION_NAME,
                points=[
                    models.PointStruct(
                        id=point_id,
                        vector=vector,
                        payload={
                            "text": chunk.page_content,
                            "source": chunk.metadata.get("source", "Unknown"),
                        },
                    )
                ],
                wait=True,
            )
        print(f"Ingested batch {i // batch_size + 1}/{(len(chunks) + batch_size - 1) // batch_size}")

    if db_conn:
        db_conn.close()
    print("Web data ingestion complete.")


if __name__ == "__main__":
    main()