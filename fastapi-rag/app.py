# fastapi-rag/app.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables (API keys, connection strings) from .env file
load_dotenv()

app = FastAPI(
    title="Physical AI RAG Service",
    description="Backend service for retrieving relevant content chunks and performing cognitive planning."
)

# --- CORS Configuration ---
# Allows the Docusaurus frontend (running on a different port/host) to communicate with this API
origins = [
    "http://localhost:3000",  # Default Docusaurus dev port
    "http://localhost:8000",
    "https://your-organization.github.io" # Production domain (for T-012 deployment)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 🧠 Health Check Endpoint ---
@app.get("/")
def read_root():
    """A simple health check to ensure the service is running."""
    return {"status": "ok", "service": "RAG Backend", "version": "0.1"}

from pydantic import BaseModel
from vector_db import get_qdrant_client, COLLECTION_NAME
from openai import OpenAI
import os

# --- Pydantic Models for API Requests ---
class QueryRequest(BaseModel):
    """Request model for the /query endpoint."""
    query: str
    limit: int = 5

# --- 🧠 Main RAG Query Endpoint ---
@app.post("/query")
async def rag_query(request: QueryRequest):
    """
    Performs a RAG query:
    1. Generates a vector embedding for the user's query.
    2. Searches the Qdrant vector database for the most similar content chunks.
    3. Returns the top matching results.
    """
    qdrant_client = get_qdrant_client()
    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # 1. Generate embedding for the query
    embedding_response = openai_client.embeddings.create(
        input=request.query,
        model="text-embedding-3-small"
    )
    query_vector = embedding_response.data[0].embedding

    # 2. Search Qdrant for similar vectors
    search_results = qdrant_client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=request.limit,
        with_payload=True  # Include the document's metadata
    )

    # 3. Format and return the results
    results = [
        {
            "id": hit.id,
            "score": hit.score,
            "text": hit.payload.get("text"),
            "source": hit.payload.get("source")
        }
        for hit in search_results
    ]
    return {"results": results}


if __name__ == "__main__":
    import uvicorn
    # Command to run the service locally: uvicorn app:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
