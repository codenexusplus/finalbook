import requests
from bs4 import BeautifulSoup

# Test accessing the sitemap
sitemap_url = "https://finalbook-ss4z.vercel.app/sitemap.xml"
print(f"Checking sitemap at: {sitemap_url}")

try:
    response = requests.get(sitemap_url)
    print(f"Status code: {response.status_code}")
    
    if response.status_code == 200:
        print("Sitemap found!")
        # Parse the sitemap to list URLs
        soup = BeautifulSoup(response.text, 'xml')
        urls = soup.find_all('loc')
        print(f"Found {len(urls)} URLs in the sitemap")
        
        # Show first few URLs
        for i, url in enumerate(urls[:10]):  # Show first 10 URLs
            print(f"  {i+1}. {url.text}")
        
        if len(urls) > 10:
            print(f"  ... and {len(urls)-10} more URLs")
    else:
        print(f"Sitemap not accessible, status code: {response.status_code}")
        
except Exception as e:
    print(f"Error accessing sitemap: {e}")