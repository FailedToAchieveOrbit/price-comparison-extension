import unittest
from product_matching.product_matcher import ProductMatcher
from product_matching.product_identifier import extract_asin, extract_upc

class TestProductMatching(unittest.TestCase):

    def test_match_identifiers(self):
        products = [
            {'title': 'Product A', 'price': 10, 'identifier': 'B00ABCDE1'},
            {'title': 'Product B', 'price': 15, 'identifier': 'B00ABCDE2'},
            {'title': 'Product C', 'price': 12, 'identifier': 'B00ABCDE3'}
        ]
        target_product = {'title': 'Product A', 'price': 10, 'identifier': 'B00ABCDE1'}
        matcher = ProductMatcher(products)
        matched_products = matcher.match_products(target_product)
        self.assertEqual(len(matched_products), 1)
        self.assertEqual(matched_products[0]['identifier'], target_product['identifier'])

    def test_extract_asin(self):
        url = "https://www.amazon.com/dp/B00ABCDE1"
        asin = extract_asin(url)
        self.assertEqual(asin, "B00ABCDE1")

    def test_extract_upc(self):
        html_content = '''
        <div>
            <b>UPC:</b> 012345678912
        </div>
        '''
        upc = extract_upc(html_content)
        self.assertEqual(upc, "012345678912")

if __name__ == '__main__':
    unittest.main()
