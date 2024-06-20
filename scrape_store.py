import requests
import xml.etree.ElementTree as ET

def scrape_urls_from_xml_url(xml_url):
    try:
        # Fetch XML content from the URL
        response = requests.get(xml_url)
        response.raise_for_status()  # Check for HTTP errors

        # Parse XML content
        root = ET.fromstring(response.content)

        # Define the namespace used in the XML
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

        # Assuming the URLs are stored inside <loc> tags
        urls = [element.text for element in root.findall('.//ns:loc', namespace)]

        return urls

    except requests.exceptions.RequestException as e:
        print(f"Error fetching XML content: {e}")
        return []

# Replace 'your_xml_url' with the actual URL of your XML file
your_xml_url = 'https://hibuddy.ca/sitemap.xml'
result = scrape_urls_from_xml_url(your_xml_url)

# Print the extracted URLs
for url in result:
    if url.startswith('https://hibuddy.ca/store/'):
        print(url)
        
