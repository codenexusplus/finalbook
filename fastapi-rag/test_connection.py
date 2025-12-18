"""
Direct test to check Qdrant connection
"""
import requests
import os
from dotenv import load_dotenv

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

print(f"Testing connection to: {QDRANT_URL}")

# Make a simple request to check the connection
try:
    # The URL already contains https:// and port, use as is but just replace /collections at the end
    test_url = f"{QDRANT_URL}/collections"

    # Test the health endpoint
    response = requests.get(
        test_url,
        headers={
            "api-key": QDRANT_API_KEY
        },
        timeout=10
    )
    
    print(f"Response Status: {response.status_code}")
    print(f"Response Text: {response.text}")
    
    if response.status_code == 200:
        print("[SUCCESS] Qdrant connection successful!")
        collections_data = response.json()
        print(f"Collections: {collections_data}")
    elif response.status_code == 403:
        print("[ERROR] 403 Forbidden - This usually means:")
        print("  1. Invalid API key")
        print("  2. Expired API key")
        print("  3. Incorrect URL")
        print("  4. Network/firewall blocking request")
    else:
        print(f"[ERROR] Unexpected status code: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"[ERROR] Request failed: {e}")
    
except Exception as e:
    print(f"[ERROR] An error occurred: {e}")