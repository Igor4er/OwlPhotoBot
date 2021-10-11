from bs4 import BeautifulSoup
import requests
from exception import *


def get_html(url, headers):
    try:
        x = requests.get(url, headers=headers)
    except ConnectionError as f:
        print(f)
        raise IdiNahuyException
    return x


def parse_owl_images(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('img', class_='MosaicAsset-module__thumb___YJI_C')
    images = []
    for item in items:
        images += [item['src']]
    return images


def get_owl_photo(url, headers):
    try:
        x = requests.get(url, headers=headers)
    except ConnectionError as f:
        print(f)
        raise IdiNahuyException
    return x
