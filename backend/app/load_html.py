import logging
import requests

from bs4 import BeautifulSoup


def load_html_page(url_loc: str) -> BeautifulSoup:
    # from pprint import pprint
    logging.debug(url_loc[1])
    url_to_request = url_loc[1]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    url_request = requests.get(url=url_to_request, headers=headers)
    logging.debug(f"REQUESTS status code: {url_request.status_code}")
    if url_request.status_code != 200:
        raise Exception("Error retrieving source code")
    url_data = url_request.content
    # pprint(url_data)
    soup = BeautifulSoup(url_data, "html.parser")
    # pprint(soup)
    return soup


def fetch_stock_item(soup: BeautifulSoup) -> str:
    logging.debug(soup.find("div", "products-area"))
    head_tag = soup.find("div", "products-area")
    logging.debug(head_tag.name)
    logging.debug(head_tag.contents)
    cupos = head_tag.find("p", "stock").contents[0]
    logging.debug(cupos)
    return cupos
