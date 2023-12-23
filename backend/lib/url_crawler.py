import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin

from lib.logger import Logger

logger = Logger()


class Crawler:
    def __init__(self, urls: list = []):
        self.visited_urls = []
        self.urls_to_visit = urls

    def download_url(self, url):
        return requests.get(url).text

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all("a"):
            path = link.get("href")
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def add_url_to_visit(self, url):
        if url not in self.visited_urls and url not in self.urls_to_visit:
            logger.debug(f"Appending URL {url}")
            self.urls_to_visit.append(url)

    def crawl(self, url):
        html = self.download_url(url)
        logger.debug(html)
        for url in self.get_linked_urls(url, html):
            self.add_url_to_visit(url)

    def yield_urls(self):
        return self.visited_urls

    def run(self):
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logger.info(f"Crawling: {url}")
            try:
                self.crawl(url)
            except Exception:
                logger.exception(f"Failed to crawl: {url}")
            finally:
                self.visited_urls.append(url)
