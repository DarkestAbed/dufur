# backend/app/load_html.py
import requests

from bs4 import BeautifulSoup

from backend.assets.config import LOGGING_LEVEL_CONSOLE
from shared.logger import Logger

logger: Logger = Logger(console_log_level=LOGGING_LEVEL_CONSOLE)


def load_html_page(url_loc: str) -> BeautifulSoup:
    # from pprint import pprint
    logger.logger.debug(url_loc[1])
    url_to_request = url_loc[1]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    url_request = requests.get(url=url_to_request, headers=headers)
    logger.logger.debug(f"REQUESTS status code: {url_request.status_code}")
    if url_request.status_code != 200:
        raise Exception("Error retrieving source code")
    url_data = url_request.content
    # pprint(url_data)
    soup = BeautifulSoup(url_data, "html.parser")
    # pprint(soup)
    return soup


def fetch_stock_item(soup: BeautifulSoup) -> str:
    # logger.logger.debug(soup.find("div", "products-area"))
    head_tag = soup.find("div", "products-area")
    # logger.logger.debug(head_tag.name)
    # logger.logger.debug(head_tag.contents)
    cupos = head_tag.find("p", "stock").contents[0]
    logger.logger.debug(cupos)
    return cupos


def fetch_class_name(soup: BeautifulSoup) -> str:
    title_tag = soup.find("div", "products-details")
    nombre_clase = title_tag.find("h3", "product_title").contents[0]
    logger.logger.debug(nombre_clase)
    return nombre_clase
