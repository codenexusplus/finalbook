# Research: RAG Query API Technology

**Date**: 2025-12-15
**Feature**: [RAG Query API](spec.md)

This document records the research and decisions for the technology stack of the RAG Query API.

## 1. API Framework

-   **Decision**: FastAPI
-   **Rationale**: The existing project structure already includes a `fastapi-rag/` directory, indicating a predisposition towards FastAPI. It's a modern, fast (high-performance) web framework for building APIs with Python, based on standard Python type hints. Its automatic OpenAPI documentation generation is a significant advantage.
-   **Alternatives considered**: None explicitly, given the existing project context.

## 2. Core Libraries

### Web Server Gateway Interface (WSGI)

-   **Decision**: `uvicorn`
-   **Rationale**: `uvicorn` is an ASGI web server implementation for Python. It is commonly used with FastAPI for high-performance asynchronous operations, leveraging `asyncio`.
-   **Alternatives considered**: None, as it's the standard for FastAPI.

### Embedding Generation (for user query)

-   **Decision**: `cohere` client library.
-   **Rationale**: Consistent with the ingestion pipeline and explicit user instruction to use Cohere for embeddings. The Cohere `embed-english-v3.0` model will be used for embedding user queries.
-   **Alternatives considered**: `openai` (constitutionally approved), but overridden by user request.

### Vector Database Client (for context retrieval)

-   **Decision**: `qdrant-client` library.
-   **Rationale**: Consistent with the ingestion pipeline and explicit user instruction to use Qdrant for vector storage. The `qdrant-client` provides the necessary functionalities to perform similarity searches.
-   **Alternatives considered**: None, as it's directly tied to the chosen vector database.

### Large Language Model (for answer generation)

-   **Decision**: `cohere` client library.
-   **Rationale**: Explicit user instruction to use Cohere for answer generation. The Cohere Command model will be used.
-   **Alternatives considered**: `openai` (constitutionally approved), but overridden by user request.

### Environment Variable Management

-   **Decision**: `python-dotenv`
-   **Rationale**: Standard practice for managing environment variables in Python projects, allowing secure loading of API keys and configurations from a `.env` file.
-   **Alternatives considered**: Manual `os.getenv()` calls, but `python-dotenv` simplifies management.

## 3. Basic Usage Patterns

### FastAPI Endpoint Structure

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query_rag(request: QueryRequest):
    # Logic for embedding, Qdrant search, LLM generation
    return {"answer": "...", "sources": ["..." ]}
```

### Cohere Embedding Usage (for query)

```python
import cohere
# cohere_client initialized globally with API_KEY

def embed_query(query_text: str) -> list[float]:
    response = cohere_client.embed(
        texts=[query_text],
        model='embed-english-v3.0',
        input_type='search_query' # Important: use search_query for query embeddings
    )
    return response.embeddings[0]
```

### Qdrant Search Usage

```python
from qdrant_client import QdrantClient, models
# qdrant_client initialized globally with URL and API_KEY
# collection_name = "rag_embedding"

def search_qdrant(query_vector: list[float], top_k: int = 5):
    search_result = qdrant_client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=top_k,
        append_payload=True
    )
    return search_result # Contains relevant text and source URLs in payload
```

### Cohere Generation Usage

```python
import cohere
# cohere_client initialized globally with API_KEY

def generate_answer(question: str, context: str) -> str:
    prompt = f"Based on the following context, answer the question.\n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:"
    response = cohere_client.generate(
        prompt=prompt,
        model='command', # Or 'command-light', 'command-r', etc.
        max_tokens=200,
        temperature=0.7
    )
    return response.generations[0].text
```
