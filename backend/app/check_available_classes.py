from lib.url_crawler import Crawler
from lib.logger import Logger

logger = Logger()


def check_classes_test():
    base_url = "https://nataliadufuur.com/clases-presenciales/"
    crawler = Crawler(urls=[base_url])
    crawler.run()
    urls = crawler.yield_urls()
    for url in urls:
        logger.debug(url)
