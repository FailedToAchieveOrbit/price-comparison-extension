from flask import Flask, request, jsonify
from web_scraping import AmazonScraper, EbayScraper

app = Flask(__name__)

@app.route('/api/get_cheapest_price', methods=['POST'])
def get_cheapest_price():
    url = request.json['url']

    if 'amazon' in url:
        scraper = AmazonScraper()
    elif 'ebay' in url:
        scraper = EbayScraper()
    else:
        return jsonify({"error": "Invalid URL. Please enter an Amazon or eBay product URL."}), 400

    product_info = scraper.get_product_info(url)
    return jsonify(product_info)

if __name__ == '__main__':
    app.run(debug=True)
