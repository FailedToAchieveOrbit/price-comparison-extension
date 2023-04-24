# ebay_scraper.py
import re
from urllib.parse import urljoin
from .scraper import Scraper

class EbayScraper(Scraper):
    def __init__(self):
        super().__init__('https://www.ebay.com')

    def get_product_details(self, product_url):
        content = self.fetch_page(product_url)
        if not content:
            return None

        soup = self.parse_html(content)

        title = soup.find('h1', {'class': 'it-ttl'}).text.strip()
        title = re.sub(r'^Details about', '', title).strip()
        price = soup.find('span', {'id': 'prcIsum'})
        if price:
            price = float(re.sub(r'[^\d.]', '', price.text.strip()))

        product_data = {
            'title': title,
            'price': price,
        }

        return product_data

    def search_similar_products(self, product_data):
        search_query = product_data['title']
        search_url = f"{self.base_url}/sch/i.html?_nkw={search_query}"
        content = self.fetch_page(search_url)
        if not content:
            return []

        soup = self.parse_html(content)
        search_results = soup.find_all('li', {'class': 's-item'})

        similar_products = []
        for result in search_results:
            link = result.find('a', {'class': 's-item__link'})
            if link:
                product_url = link['href']
                product_data = self.get_product_details(product_url)
                similar_products.append(product_data)

        return similar_products
