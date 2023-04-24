from web_scraping import AmazonScraper, EbayScraper
from utils.common_utils import merge_dicts

def find_cheapest_product(url: str) -> dict:
    if 'amazon' in url:
        scraper = AmazonScraper()
    elif 'ebay' in url:
        scraper = EbayScraper()
    else:
        raise ValueError('Unsupported website')

    product_info = scraper.get_product_info(url)
    alternative_products = scraper.get_similar_products(product_info)
    sorted_products = sorted(alternative_products, key=lambda x: x['price'])

    return {
        'product_info': product_info,
        'sorted_alternatives': sorted_products
    }


if __name__ == '__main__':
    # Example usage
    url = 'https://www.amazon.com/example-product'
    results = find_cheapest_product(url)
    print(results)
    #when testing is over... we will need to remove main.py and create api.py