import re

def extract_asin(url):
    asin_pattern = r"(?<=dp/)[A-Z0-9]{10}|(?<=dp%2F)[A-Z0-9]{10}"
    match = re.search(asin_pattern, url)
    return match.group(0) if match else None

def extract_upc(html_content):
    upc_pattern = r"UPC:</b>\s*([0-9]{12})"
    match = re.search(upc_pattern, html_content)
    return match.group(1) if match else None
