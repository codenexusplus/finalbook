# Research: Embedding Pipeline Technology

**Date**: 2025-12-15
**Feature**: [Embedding Pipeline Setup](spec.md)

This document records the research and decisions for the technology stack of the embedding pipeline.

## 1. Programming Language and Environment

-   **Decision**: Python 3.11+
-   **Rationale**: The user prompt specified `pip packages` and a `main.py` file, clearly indicating a Python environment. Python has a rich ecosystem of libraries for web scraping, API interaction, and data processing, making it the ideal choice for this task.
-   **Alternatives considered**: None. The user's request was specific.

## 2. Core Libraries

### Web Crawling and Parsing

-   **Decision**: `requests` and `BeautifulSoup4`.
-   **Rationale**:
    -   `requests` is the de-facto standard for making HTTP requests in Python. It is simple, reliable, and well-documented.
    -   `BeautifulSoup4` is a powerful and Pythonic library for pulling data out of HTML and XML files. It excels at parsing web content and navigating the parse tree.
-   **Alternatives considered**:
    -   `Scrapy`: A more powerful, asynchronous crawling framework. It was rejected as overkill for this project's scope, which focuses on a single site. `requests` + `BeautifulSoup4` provides a simpler, synchronous approach that is sufficient.

### Embedding Generation

-   **Decision**: `cohere` client library.
-   **Rationale**: The user explicitly requested the use of **Cohere**. The official `cohere` Python library is the correct tool for interacting with their API.
-   **Alternatives considered**:
    -   `openai`: This is the constitutionally approved alternative. It was rejected to align with the user's direct request. **This decision requires a constitution amendment to be fully compliant.**

### Vector Database

-   **Decision**: `qdrant-client` library.
-   **Rationale**: The user explicitly requested the use of **Qdrant**. The `qdrant-client` is the official Python SDK for interacting with Qdrant Cloud and managing vector collections.
-   **Alternatives considered**: None. The user's request was specific.

## 3. Basic Usage Patterns

### Cohere Client

```python
import cohere
co = cohere.Client('YOUR_COHERE_API_KEY') # from .env

def embed(texts: list[str]):
    response = co.embed(
        texts=texts,
        model='embed-english-v3.0',
        input_type='search_document'
    )
    return response.embeddings
```

### Qdrant Client

```python
from qdrant_client import QdrantClient, models

# Initialize client
client = QdrantClient(url="YOUR_QDRANT_URL", api_key="YOUR_QDRANT_API_KEY") # from .env
collection_name = "rag_embedding"

# Create collection if it doesn't exist
try:
    client.get_collection(collection_name=collection_name)
except Exception:
    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE), # Size for embed-english-v3.0
    )

# Upsert vectors
def save_to_qdrant(vectors, texts, sources):
    client.upsert(
        collection_name=collection_name,
        points=models.Batch(
            ids=[...], # generate unique IDs
            vectors=vectors,
            payloads=[{"text": text, "source": source} for text, source in zip(texts, sources)]
        )
    )
```
