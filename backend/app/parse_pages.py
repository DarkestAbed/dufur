import json
import logging
import os


def get_pages_from_json(pages_loc: str = None) -> dict:
    from pprint import pprint
    logging.info("Loading static assets...")
    if pages_loc is None:
        pages_loc = os.path.join(os.getcwd(), "assets", "cursos.json")
        logging.debug(pages_loc)
    logging.debug(os.path.exists(path=pages_loc))
    if not os.path.exists(path=pages_loc):
        raise Exception("No JSON file located")
    with open(file=pages_loc, mode="r") as file:
        dict_pages = json.load(file)
    logging.debug(dict_pages)
    return dict_pages


def parse_pages(pages_dict: dict) -> dict:
    # from pprint import pprint
    logging.info("Parsing data from static assets...")
    base_url = "https://nataliadufuur.com/product"
    new_dict = {}
    idx = 0
    for key, item in pages_dict.items():
        if isinstance(item, list):
            for page in item:
                logging.debug(f"{key}: {base_url}/{page}")
                new_dict[idx] = {
                    "category": key,
                    "base_page": page,
                    "full_page": f"{base_url}/{page}",
                }
                idx += 1
        else:
            pass
            logging.debug(f"{key}: {item}")
    logging.debug(new_dict)
    return new_dict


def retrieve_page(pages_dict: dict, idx: int) -> str:
    return (pages_dict[idx]["category"], pages_dict[idx]["full_page"])
