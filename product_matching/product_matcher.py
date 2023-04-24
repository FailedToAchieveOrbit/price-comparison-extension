import re
from nlp_processing.nlp_utils import compare_titles

class ProductMatcher:
    def __init__(self, products):
        self.products = products

    def match_products(self, target_product):
        matched_products = []
        target_title = target_product['title']
        target_identifier = target_product['identifier']

        for product in self.products:
            if self.match_identifiers(target_identifier, product['identifier']):
                matched_products.append(product)
            elif compare_titles(target_title, product['title']):
                matched_products.append(product)

        return matched_products

    @staticmethod
    def match_identifiers(identifier1, identifier2):
        return identifier1 and identifier2 and identifier1 == identifier2
