# backend/app/parse_pages.py
import json
import os

from backend.assets.config import LOGGING_LEVEL_CONSOLE
from shared.logger import Logger

logger: Logger = Logger(console_log_level=LOGGING_LEVEL_CONSOLE)


def get_pages_from_json(pages_loc: str = None) -> dict:
    # from pprint import pprint
    if pages_loc is None:
        pages_loc = os.path.join(os.getcwd(), "backend", "assets", "cursos.json")
        logger.logger.debug(pages_loc)
    logger.logger.debug(os.path.exists(path=pages_loc))
    if not os.path.exists(path=pages_loc):
        raise Exception("No JSON file located")
    with open(file=pages_loc, mode="r") as file:
        dict_pages = json.load(file)
    logger.logger.debug(dict_pages)
    return dict_pages


def parse_pages_from_dict(pages_dict: dict) -> dict:
    # from pprint import pprint
    base_url = "https://nataliadufuur.com/product"
    new_dict = {}
    idx = 0
    for key, item in pages_dict.items():
        if isinstance(item, list):
            for page in item:
                full_page: str = f"{base_url}/{page}" if "nataliadufuur" not in page else f"{page}"
                logger.logger.debug(f"{key}: {full_page}")
                new_dict[idx] = {
                    "day_of_week": key,
                    "base_page": page,
                    "full_page": full_page,
                }
                idx += 1
        else:
            pass
            logger.logger.debug(f"{key}: {item}")
    logger.logger.debug(new_dict)
    return new_dict


def retrieve_page(pages_dict: dict, idx: int) -> str:
    return (pages_dict[idx]["day_of_week"], pages_dict[idx]["full_page"])


def parse_pages(pages_loc: str = None) -> dict:
    logger.logger.info("Loading static assets...")
    try:
        dict_pages = get_pages_from_json(pages_loc=pages_loc)
        logger.logger.info("Pages loaded. Proceeding...")
    except Exception:
        logger.logger.critical("Error getting classes asset")
        raise Exception
    logger.logger.debug(dict_pages)
    logger.logger.info("Parsing data from static assets...")
    try:
        dict_pages = parse_pages_from_dict(pages_dict=dict_pages)
        logger.logger.info("Data parsed. Proceeding...")
    except Exception:
        logger.logger.critical("Error parsing classes data")
        raise Exception
    return dict_pages
