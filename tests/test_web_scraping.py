import unittest
from web_scraping import AmazonScraper, EbayScraper

class TestWebScraping(unittest.TestCase):
    def test_amazon_scraper(self):
        scraper = AmazonScraper()
        product_info = scraper.get_product_info('https://www.amazon.com/example-product')
        self.assertEqual(product_info['title'], 'Example title')
        self.assertEqual(product_info['price'], 29.99)

    def test_ebay_scraper(self):
        scraper = EbayScraper()
        product_info = scraper.get_product_info('https://www.ebay.com/example-product')
        self.assertEqual(product_info['title'], 'Example title')
        self.assertEqual(product_info['price'], 29.99)

if __name__ == '__main__':
    unittest.main()
