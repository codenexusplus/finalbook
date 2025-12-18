import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
from dotenv import load_dotenv
import cohere
from vector_db import query_qdrant

from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
load_dotenv()

# Initialize clients
cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))

app = FastAPI()

# Add CORS middleware
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    sources: List[str] = []

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    """
    Performs Retrieval-Augmented Generation (RAG) to answer a question.
    """
    try:
        # 1. Get relevant documents from Qdrant
        search_results = query_qdrant(query=request.question, cohere_client=cohere_client)
        
        if not search_results:
            # Fallback if no relevant documents are found
            return QueryResponse(answer="I'm sorry, I couldn't find any relevant information to answer your question.", sources=[])

        # 2. Format documents for Cohere's chat method
        documents = [
            {"title": result.payload.get("source", ""), "snippet": result.payload.get("text", "")}
            for result in search_results
        ]
        
        # 3. Generate response using Cohere
        response = cohere_client.chat(
            model="command-r",
            message=request.question,
            documents=documents
        )
        answer = response.text
        
        # Extract source URLs from the search results
        source_urls = list(set([doc["title"] for doc in documents if doc["title"]]))

        return QueryResponse(answer=answer, sources=source_urls)

    except Exception as e:
        print(f"Error during RAG query: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while processing your request.")
