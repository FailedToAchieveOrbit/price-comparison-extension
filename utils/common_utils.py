import re
import requests
from typing import Dict


def sanitize_string(text: str) -> str:
    """Remove unnecessary characters from a given string."""
    return re.sub(r'\s+', ' ', text).strip()


def parse_price(price: str) -> float:
    """Convert a price string to a float."""
    return float(re.sub(r'[^\d\.]', '', price))


def get_exchange_rate(base_currency: str, target_currency: str) -> float:
    """Fetch the exchange rate between two currencies using an external API."""
    # We have to replace this URL with a real API endpoint
    url = f'https://api.example.com/exchange_rates?base={base_currency}&target={target_currency}'
    response = requests.get(url)
    data = response.json()

    return data['rate']


def convert_price(price: float, base_currency: str, target_currency: str) -> float:
    """Convert a price from one currency to another."""
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    return price * exchange_rate


def merge_dicts(dict1: Dict, dict2: Dict) -> Dict:
    """Merge two dictionaries into one."""
    result = dict1.copy()
    result.update(dict2)
    return result
