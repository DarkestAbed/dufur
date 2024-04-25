# backend/lib/url_crawler.py
import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin

from backend.assets.config import LOGGING_LEVEL_CONSOLE
from shared.logger import Logger

logger: Logger = Logger(console_log_level=LOGGING_LEVEL_CONSOLE)


class Crawler:
    def __init__(self, urls: list = []):
        self.visited_urls = []
        self.urls_to_visit = urls

    def download_url(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        return requests.get(url=url, headers=headers).text

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all("a"):
            path = link.get("href")
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def add_url_to_visit(self, url):
        # logger.logger.debug(url)
        if url is None:
            return None
        if url not in self.visited_urls and url not in self.urls_to_visit and "https" in url:
            if "product/" in url:
                logger.logger.info(f"Appending 'product/' URL: {url}")
                self.urls_to_visit.append(url)

    def crawl(self, url):
        html = self.download_url(url)
        # logger.logger.debug(html)
        for url in self.get_linked_urls(url, html):
            self.add_url_to_visit(url)

    def yield_urls(self):
        return self.visited_urls

    def run(self):
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logger.logger.info(f"Crawling: {url}")
            try:
                self.crawl(url)
            except Exception:
                logger.logger.exception(f"Failed to crawl: {url}")
            finally:
                self.visited_urls.append(url)
