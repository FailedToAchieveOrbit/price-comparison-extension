# amazon_scraper.py
import re
from urllib.parse import urljoin, quote
from .scraper import Scraper

class AmazonScraper(Scraper):
    def __init__(self):
        super().__init__('https://www.amazon.com')

    def get_product_details(self, product_url):
        content = self.fetch_page(product_url)
        if not content:
            return None

        soup = self.parse_html(content)

        title = soup.find('span', {'id': 'productTitle'}).text.strip()
        price = soup.find('span', {'id': 'priceblock_ourprice'})
        if price:
            price = float(re.sub(r'[^\d.]', '', price.text.strip()))

        product_data = {
            'title': title,
            'price': price,
        }

        return product_data

    def search_similar_products(self, product_data):
        search_query = quote(product_data['title'])
        search_url = f"{self.base_url}/s?k={search_query}"
        content = self.fetch_page(search_url)
        if not content:
            return []

        soup = self.parse_html(content)
        search_results = soup.find_all('div', {'data-index': re.compile(r'\d+')})

        similar_products = []
        for result in search_results:
            link = result.find('a', {'class': 'a-link-normal'})
            if link:
                product_url = urljoin(self.base_url, link['href'])
                product_data = self.get_product_details(product_url)
                similar_products.append(product_data)

        # Sort by price
        similar_products = sorted(similar_products, key=lambda x: x['price'])

        return similar_products
