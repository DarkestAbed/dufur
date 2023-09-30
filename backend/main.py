import logging

from app.parse_pages import get_pages_from_json, parse_pages
from app.store_data import store_process

logging.basicConfig(level=logging.INFO, format="%(asctime)s :: %(levelname)s :: %(message)s")


def main():
    dict_pages = get_pages_from_json()
    logging.debug(dict_pages)
    new_dict_pages = parse_pages(pages_dict=dict_pages)
    store_process(pages=new_dict_pages)


if __name__ == "__main__":
    main()
else:
    pass
