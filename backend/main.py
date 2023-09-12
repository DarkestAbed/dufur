import logging

from app.parse_pages import get_pages_from_json, parse_pages, retrieve_page
from app.load_html import load_html_page, fetch_stock_item
from app.store_data import store_data_in_dict

logging.basicConfig(level=logging.INFO, format="%(asctime)s :: %(levelname)s :: %(message)s")


def main():
    dict_pages = get_pages_from_json()
    logging.debug(dict_pages)
    new_dict_pages = parse_pages(pages_dict=dict_pages)
    logging.debug(new_dict_pages)
    for index in range(0, 3):
        page = retrieve_page(pages_dict=new_dict_pages, idx=index)
        # logging.info(page)
        # print(f"{index + 1} : {page}")
        soup = load_html_page(page)
        cupos_disponibles = fetch_stock_item(soup=soup)
        # print(f"Cupos disponibles? : {cupos_disponibles}")
        store_data_in_dict(page=page, availability=cupos_disponibles)


if __name__ == "__main__":
    main()
else:
    pass
