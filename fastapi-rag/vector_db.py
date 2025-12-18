# fastapi-rag/vector_db.py

import os
from qdrant_client import QdrantClient, models
from dotenv import load_dotenv

load_dotenv()

# --- Configuration (from .env) ---
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = os.getenv("QDRANT_COLLECTION_NAME") or os.getenv("COLLECTION_NAME", "rag_embedding")

# --- Embedding Model Dimension ---
# Using the standard dimensions for Cohere's embed-english-v3.0 model (1024)
VECTOR_DIMENSION = 1024

def get_qdrant_client():
    """Returns the configured Qdrant client instance."""
    if not QDRANT_URL or not QDRANT_API_KEY:
        raise ValueError("QDRANT_URL or QDRANT_API_KEY not set in .env")

    return QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        https=True
    )

def create_qdrant_collection(client: QdrantClient) -> str:
    """
    Creates the Qdrant collection if it doesn't already exist.
    """
    try:
        # Check if the collection exists to avoid recreation errors
        collections = client.get_collections().collections
        if COLLECTION_NAME in [c.name for c in collections]:
            print(f"   Collection '{COLLECTION_NAME}' already exists. Skipping creation.")
            return COLLECTION_NAME

        print(f"Creating Qdrant collection '{COLLECTION_NAME}' with dimension {VECTOR_DIMENSION}...")
        
        # Define the collection configuration
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=VECTOR_DIMENSION, distance=models.Distance.COSINE),
            # Set up indexing for metadata payload (useful for filtering/pre-filtering)
            # The 'id' payload will link directly to the Neon Postgres ID
            optimizers_config=models.OptimizersConfig(
                memmap_threshold=20000 # Recommended setting for free-tier optimization
            )
        )
        print(f"✅ Success: Qdrant collection '{COLLECTION_NAME}' created.")
        return COLLECTION_NAME

    except Exception as e:
        print(f"❌ Error creating Qdrant collection: {e}")
        raise

def query_qdrant(query: str, cohere_client, top_k: int = 5):
    """
    Queries the Qdrant collection for similar documents.
    """
    if not query:
        return []

    try:
        # Generate the query embedding
        query_embedding = cohere_client.embed(
            texts=[query],
            model='embed-english-v3.0',
            input_type='search_query'
        ).embeddings[0]

        qdrant_client = get_qdrant_client()
        
        print(f"DEBUG: Type of qdrant_client: {type(qdrant_client)}")
        print(f"DEBUG: dir(qdrant_client): {dir(qdrant_client)}")
        
        # Search for similar vectors in the collection
        search_result = qdrant_client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_embedding,
            limit=top_k,
            with_payload=True # Include the payload in the search results
        )
        
        return search_result

    except Exception as e:
        print(f"❌ Error querying Qdrant: {e}")
        return []

if __name__ == "__main__":
    qdrant_client = get_qdrant_client()
    create_qdrant_collection(qdrant_client)
    # The client instance is now ready for use in the ingestion script (T-016)
