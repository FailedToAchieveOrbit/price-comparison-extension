# scraper.py
import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_page(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
        return None

    def parse_html(self, html_content):
        return BeautifulSoup(html_content, 'html.parser')
