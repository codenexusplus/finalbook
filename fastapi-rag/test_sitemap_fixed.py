import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_sitemap_urls(sitemap_url, base_domain=None):
    """Extract URLs from a sitemap.xml file"""
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'xml')  # Use xml parser for sitemaps
        urls = []
        
        # Look for <url><loc> elements in the sitemap
        for url_element in soup.find_all('loc'):
            url = url_element.text.strip()
            
            # If base_domain is provided and URL contains localhost, replace with actual domain
            if base_domain and "localhost" in url:
                # Replace localhost:3000 with the actual domain
                url = url.replace("localhost:3000", base_domain.replace("https://", "").replace("http://", ""))
            elif base_domain and "127.0.0.1" in url:
                # Also handle 127.0.0.1
                url = url.replace("127.0.0.1:3000", base_domain.replace("https://", "").replace("http://", ""))
            
            urls.append(url)
        
        # Also look for sitemaps within sitemaps (sitemap index)
        for sitemap_element in soup.find_all('sitemap'):
            loc = sitemap_element.find('loc')
            if loc:
                sub_sitemap_url = loc.text.strip()
                
                # Update sub-sitemap URL if localhost is present
                if base_domain and "localhost" in sub_sitemap_url:
                    sub_sitemap_url = sub_sitemap_url.replace("localhost:3000", base_domain.replace("https://", "").replace("http://", ""))
                
                print(f"Found sub-sitemap: {sub_sitemap_url}")
                # Recursively get URLs from sub-sitemaps
                sub_urls = get_sitemap_urls(sub_sitemap_url, base_domain)
                urls.extend(sub_urls)
        
        return urls
    except Exception as e:
        print(f"Error parsing sitemap {sitemap_url}: {e}")
        return []

# Test accessing the sitemap with domain transformation
base_url = "https://finalbook-ss4z.vercel.app"
sitemap_url = f"{base_url}/sitemap.xml"
print(f"Checking sitemap at: {sitemap_url}")

try:
    urls = get_sitemap_urls(sitemap_url, base_url)
    print(f"Found {len(urls)} URLs in the sitemap after domain transformation")
    
    # Show first few URLs
    for i, url in enumerate(urls[:10]):  # Show first 10 URLs
        print(f"  {i+1}. {url}")
    
    if len(urls) > 10:
        print(f"  ... and {len(urls)-10} more URLs")
        
except Exception as e:
    print(f"Error accessing sitemap: {e}")