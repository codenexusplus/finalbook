import os
from dotenv import load_dotenv
load_dotenv()

# Test if all required environment variables are set
required_vars = ["COHERE_API_KEY", "QDRANT_URL", "QDRANT_API_KEY"]
missing_vars = [var for var in required_vars if not os.getenv(var)]

if missing_vars:
    print(f"Warning: Missing required environment variables: {missing_vars}")
    print("Please set these in your .env file before running the ingestion.")
else:
    print("All required environment variables are set!")

# Test if VERCEL_URL is set for web ingestion
vercel_url = os.getenv("VERCEL_URL")
if vercel_url:
    print(f"Vercel URL is set: {vercel_url}")
    print("Web ingestion mode will be enabled.")
else:
    print("VERCEL_URL not set, will use local file ingestion if DOCS_PATH is set.")

# Verify langchain import works (using the community version)
try:
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    print("OK - Langchain import successful")
except ImportError as e:
    try:
        # Try the community version which is more commonly used
        from langchain_community.text_splitter import RecursiveCharacterTextSplitter
        print("OK - Langchain community import successful")
    except ImportError as e2:
        print(f"ERROR - Error importing langchain: {e} and {e2}")

# Verify other imports work
try:
    import requests
    from bs4 import BeautifulSoup
    import cohere
    from qdrant_client import QdrantClient
    print("OK - All necessary imports successful")
except ImportError as e:
    print(f"ERROR - Error importing required modules: {e}")

print("Environment verification complete!")