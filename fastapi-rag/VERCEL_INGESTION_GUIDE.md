# RAG Chatbot with Vercel URL Ingestion

This guide explains how to set up and use the RAG (Retrieval-Augmented Generation) chatbot to ingest content from a Vercel URL (like https://finalbook-ss4z.vercel.app) using Cohere and Qdrant.

## Overview

The system consists of:
1. **Data Ingestion**: Pulls content from a Vercel URL (using sitemap.xml if available)
2. **Embedding Generation**: Uses Cohere to create vector embeddings
3. **Vector Storage**: Stores embeddings in Qdrant for fast retrieval
4. **Chat Interface**: FastAPI application to query the ingested content

## Setup Instructions

### 1. Install Dependencies
```bash
cd fastapi-rag
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy the example environment file:
```bash
cp .env.example .env
```

Then edit `.env` with your specific values:

```bash
# Required: Cohere API Key for embeddings and generation
COHERE_API_KEY="your-cohere-api-key"

# Required: Qdrant Configuration for vector storage
QDRANT_URL="https://your-qdrant-instance.qdrant.tech:6333"
QDRANT_API_KEY="your-qdrant-api-key"

# Required: Vercel URL to ingest content from
VERCEL_URL="https://finalbook-ss4z.vercel.app"

# Optional: PostgreSQL database URL (if using with Neon)
# NEON_DATABASE_URL="your-postgres-db-url"

# Optional: Custom Qdrant collection name
# QDRANT_COLLECTION_NAME="rag_embedding"
```

### 3. Data Ingestion from Vercel URL

The system will automatically detect if `VERCEL_URL` is set in the environment and will:
1. First try to load content from `sitemap.xml` (with localhost URLs corrected to the actual domain)
2. If no sitemap is found, fall back to web scraping the site
3. Extract text content from HTML pages
4. Split content into chunks
5. Generate embeddings using Cohere
6. Store vector embeddings in Qdrant
7. Optionally store metadata in PostgreSQL (if configured)

To run the ingestion:
```bash
python ingest.py
```

Or use the dedicated web ingestion script:
```bash
python ingest_web.py
```

### 4. Start the API Server

Once ingestion is complete, start the FastAPI server:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### 5. Query the Chatbot

The API will be available at `http://localhost:8000`. You can:

1. Access the interactive documentation at `http://localhost:8000/docs`
2. Query via curl:

```bash
curl -X POST "http://localhost:8000/query" \
-H "Content-Type: application/json" \
-d '{
  "question": "What is ROS 2?"
}'
```

## Technical Details

### Sitemap Handling
- The system automatically fetches `sitemap.xml` from the provided Vercel URL
- Corrects any localhost URLs to the actual domain 
- Processes up to 29 URLs found in the sitemap for the provided example site

### Content Processing
- Extracts text from HTML, ignoring scripts and style tags
- Uses RecursiveCharacterTextSplitter with:
  - Chunk size: 1000 characters
  - Overlap: 150 characters
- Generates embeddings using Cohere's `embed-english-v3.0` model

### Vector Storage
- Uses Qdrant as the vector database
- Stores chunks with their embeddings and source URLs
- Uses cosine distance for similarity search

## Configuration Options

You can customize the system behavior by adjusting these environment variables:

- `CHUNK_SIZE`: Size of text chunks (default: 1000)
- `CHUNK_OVERLAP`: Overlap between chunks (default: 150)
- `VERCEL_URL`: Source URL to scrape (required for web ingestion)
- `DOCS_PATH`: Local directory to ingest from (alternative to VERCEL_URL)

## Troubleshooting

1. **Sitemap not found**: The system will fall back to web scraping but be more limited
2. **Rate limiting**: The system includes reasonable delays to respect the source site
3. **Missing environment variables**: The system will show clear error messages
4. **Qdrant connection issues**: Verify your URL and API key are correct

## Example Questions to Try

Once your system is running, try questions like:
- "What are the key concepts in ROS 2?"
- "Explain the architecture of ROS 2"
- "How do I create a Python agent with rclpy?"

The chatbot will use your Vercel-hosted content to generate informed responses with source citations.