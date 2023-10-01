import logging

from app.parse_pages import parse_pages
from app.store_data import store_process

logging.basicConfig(level=logging.INFO, format="%(asctime)s :: %(levelname)s :: %(message)s")


def main():
    dict_pages = parse_pages(pages_loc=None)
    dict_data = store_process(pages=dict_pages)


if __name__ == "__main__":
    main()
else:
    pass
