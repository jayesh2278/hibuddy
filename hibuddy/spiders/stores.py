import scrapy
import xml.etree.ElementTree as ET
from scrapy.crawler import CrawlerProcess
from scrapy.http import XmlResponse

class StoresSpider(scrapy.Spider):
    name = "stores"
    def start_requests(self):
        # Replace 'your_xml_url' with the actual URL of your XML file
        your_xml_url = 'https://hibuddy.ca/sitemap.xml'
        yield scrapy.Request(url=your_xml_url, callback=self.parse)

    def parse(self, response):
        try:
            # Parse XML content using XmlResponse
            xml_response = XmlResponse(url=response.url, body=response.body, encoding='utf-8')

            # Define the namespace used in the XML
            namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

            # Assuming the URLs are stored inside <loc> tags
            urls = xml_response.xpath('//ns:loc/text()', namespaces=namespace).extract()

            # Print the extracted URLs
            for url in urls:
                if url.startswith('https://hibuddy.ca/store/'):
                    yield{
                        'url':url
                    }

        except Exception as e:
            self.log(f"Error parsing XML content: {e}")
