"""
Debugging script to test RAG functionality
"""
import os
import sys
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

print("Environment variables check:")
print(f"COHERE_API_KEY: {'SET' if os.getenv('COHERE_API_KEY') else 'NOT SET'}")
print(f"QDRANT_URL: {os.getenv('QDRANT_URL')}")
print(f"QDRANT_API_KEY: {'SET' if os.getenv('QDRANT_API_KEY') else 'NOT SET'}")
print(f"COLLECTION_NAME: {os.getenv('COLLECTION_NAME', os.getenv('QDRANT_COLLECTION_NAME', 'default-collection'))}")

from vector_db import query_qdrant, get_qdrant_client
import cohere

def test_connection():
    print("\nTesting connections...")
    
    # Test Cohere
    try:
        cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))
        print("✅ Cohere client initialized successfully")
    except Exception as e:
        print(f"❌ Error initializing Cohere client: {e}")
        return False
    
    # Test Qdrant
    try:
        client = get_qdrant_client()
        collections = client.get_collections()
        print(f"✅ Qdrant connection successful. Available collections: {[col.name for col in collections.collections]}")
        
        # Check if our collection exists
        COLLECTION_NAME = os.getenv("QDRANT_COLLECTION_NAME") or os.getenv("COLLECTION_NAME", "default-collection")
        collection_exists = COLLECTION_NAME in [col.name for col in collections.collections]
        print(f"Collection '{COLLECTION_NAME}' exists: {collection_exists}")
        
        if collection_exists:
            # Count points in the collection
            count = client.count(collection_name=COLLECTION_NAME)
            print(f"Number of points in collection: {count.count}")
        
    except Exception as e:
        print(f"❌ Error connecting to Qdrant: {e}")
        return False
        
    return True

def test_query():
    print("\nTesting query functionality...")
    
    cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))
    COLLECTION_NAME = os.getenv("QDRANT_COLLECTION_NAME") or os.getenv("COLLECTION_NAME", "default-collection")
    
    # Test a simple query
    test_question = "What is this book about?"
    results = query_qdrant(query=test_question, cohere_client=cohere_client)
    
    print(f"\nTest question: {test_question}")
    print(f"Number of results retrieved: {len(results) if results else 0}")
    
    if results:
        for i, result in enumerate(results[:2]):  # Show first 2 results
            print(f"Result {i+1}:")
            print(f"  Score: {result.score}")
            print(f"  Text preview: {result.payload.get('text', '')[:100]}...")
            print(f"  Source: {result.payload.get('source', 'Unknown')}")
    else:
        print("No results found. This could mean:")
        print("- The collection is empty")
        print("- The collection name doesn't match")
        print("- There was an error during the query")
    
    return len(results) > 0

if __name__ == "__main__":
    print("[DEBUG] Starting RAG Chatbot Debugging...")

    success = test_connection()
    if success:
        has_results = test_query()
        print(f"\n[SUMMARY]:")
        print(f"- Connection test: {'PASS' if success else 'FAIL'}")
        print(f"- Query test: {'PASS' if has_results else 'FAIL (or empty results)'}")

        if not has_results:
            print("\n[POTENTIAL SOLUTIONS]:")
            print("1. Check if your collection ('FINAL-BOOK') has been populated with data")
            print("2. Verify that the ingestion process ran successfully")
            print("3. Make sure the QDRANT_COLLECTION_NAME in environment matches your actual collection")
    else:
        print("\n[ERROR] Connection test failed. Please fix the connection issues first.")