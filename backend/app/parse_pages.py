import json
import logging
import os


def get_pages_from_json(pages_loc: str = None) -> dict:
    # from pprint import pprint
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


def parse_pages_from_dict(pages_dict: dict) -> dict:
    # from pprint import pprint
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


def parse_pages(pages_loc: str = None) -> dict:
    logging.info("Loading static assets...")
    try:
        dict_pages = get_pages_from_json(pages_loc=pages_loc)
        logging.info("Pages loaded. Proceeding...")
    except Exception:
        logging.critical("Error getting classes asset")
        raise Exception
    logging.debug(dict_pages)
    logging.info("Parsing data from static assets...")
    try:
        dict_pages = parse_pages_from_dict(pages_dict=dict_pages)
        logging.info("Data parsed. Proceeding...")
    except Exception:
        logging.critical("Error parsing classes data")
        raise Exception
    return dict_pages
