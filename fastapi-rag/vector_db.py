# fastapi-rag/vector_db.py

import os
from qdrant_client import QdrantClient, models
from dotenv import load_dotenv

load_dotenv()

# --- Configuration (from .env) ---
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = os.getenv("QDRANT_COLLECTION_NAME")

# --- Embedding Model Dimension ---
# Using the standard dimensions for OpenAI's text-embedding-3-small model (1536)
# or similar robust free-tier models (e.g., MiniLM-L6-v2 which is 384).
# We'll use 1536 for OpenAI's model.
VECTOR_DIMENSION = 1536

def get_qdrant_client():
    """Returns the configured Qdrant client instance."""
    if not QDRANT_URL or not QDRANT_API_KEY:
         raise ValueError("QDRANT_URL or QDRANT_API_KEY not set in .env")
         
    return QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY
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

if __name__ == "__main__":
    qdrant_client = get_qdrant_client()
    create_qdrant_collection(qdrant_client)
    # The client instance is now ready for use in the ingestion script (T-016)
