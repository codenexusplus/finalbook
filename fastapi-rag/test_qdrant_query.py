import os
from dotenv import load_dotenv
import cohere
import sys # Import sys to access sys.path
from vector_db import get_qdrant_client, COLLECTION_NAME, VECTOR_DIMENSION
import vector_db # Explicitly import vector_db to access its __file__ attribute

load_dotenv()

print(f"DEBUG: sys.path: {sys.path}")
print(f"DEBUG: Loaded vector_db from: {vector_db.__file__}")

# --- Configuration ---
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

def query_qdrant_direct(query: str, cohere_client, top_k: int = 5):
    """
    Queries the Qdrant collection for similar documents and prints their content.
    """
    if not query:
        print("Query cannot be empty.")
        return []

    try:
        # Generate the query embedding
        query_embedding = cohere_client.embed(
            texts=[query],
            model='embed-english-v3.0',
            input_type='search_query'
        ).embeddings[0]

        qdrant_client = get_qdrant_client()
        
        # Search for similar vectors in the collection
        search_result = qdrant_client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_embedding,
            limit=top_k,
            with_payload=True # Include the payload in the search results
        )
        
        print(f"--- Qdrant Search Results for '{query}' (Top {top_k}) ---")
        if not search_result:
            print("No results found in Qdrant.")
            return []

        for i, hit in enumerate(search_result):
            print(f"\nResult {i+1} (Score: {hit.score}):")
            print(f"  Source: {hit.payload.get('source', 'N/A')}")
            print(f"  Text: {hit.payload.get('text', 'N/A')[:500]}...") # Print first 500 chars
        
        return search_result

    except Exception as e:
        print(f"❌ Error querying Qdrant: {e}")
        return []

if __name__ == "__main__":
    if not COHERE_API_KEY:
        print("COHERE_API_KEY is not set in the .env file. Please set it to proceed.")
    else:
        cohere_client = cohere.Client(COHERE_API_KEY)
        query_qdrant_direct("define module 1", cohere_client)
        print("\n--- Testing with 'module 1' ---")
        query_qdrant_direct("module 1", cohere_client)
        print("\n--- Testing with 'ROS2' ---")
        query_qdrant_direct("ROS2", cohere_client) # Test with a known keyword from module 1
        print("\n--- Testing with 'ch1-foundations-physical-ai' ---")
        query_qdrant_direct("ch1-foundations-physical-ai", cohere_client) # Test with a specific document title
