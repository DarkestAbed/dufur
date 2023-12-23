from app.parse_pages import retrieve_page
from app.load_html import load_html_page, fetch_stock_item
from app.parse_dates import get_day_time_of_class
from assets.config import TIMESTAMP_FMT
from lib.logger import Logger

logger = Logger()


def store_data_in_dict(page: dict, availability: str) -> dict:
    from datetime import datetime
    # from pprint import pprint
    now_ts = datetime.strftime(datetime.now(), TIMESTAMP_FMT)
    logger.debug(now_ts)
    date_class = get_day_time_of_class(url=page[1])
    inside_dict = {
        "category": page[0],
        "url": page[1],
        "date_class": date_class,
        "availability": availability,
        "check_time": now_ts,
    }
    # pprint(inside_dict)
    return inside_dict


def store_all_data(pages: dict) -> dict:
    # from pprint import pprint
    logger.debug(pages)
    full_dict = {}
    for index in range(0, len(pages)):
        page = retrieve_page(pages_dict=pages, idx=index)
        logger.debug(page)
        logger.debug(f"{index + 1} : {page}")
        try:
            soup = load_html_page(page)
        except Exception as e:
            msg = f"Encontramos un error al buscar las clases, para la clase {page[0]}, URL {page[1]}"
            logger.error(msg=msg)
            next
        cupos_disponibles = fetch_stock_item(soup=soup)
        temp_data = store_data_in_dict(page=page, availability=cupos_disponibles)
        logger.debug(f"Cupos disponibles? : {temp_data.get('category')} ({temp_data.get('date_class')}) :: {temp_data.get('availability')}")
        full_dict[index] = temp_data
    # pprint(full_dict)
    return full_dict


def store_in_file(data: dict, path_to_file: str) -> None:
    import json
    try:
        with open(path_to_file, "w") as file:
            json.dump(obj=data, fp=file)
    except Exception as e:
        logger.critical(f"Error saving classes data.\nException raised was {e}")
        raise Exception("Error saving classes data")
    return None


def store_process(pages: dict, store_to_disk: bool = True) -> dict:
    import os
    # import pdb
    from datetime import datetime
    logger.info("Fetching data from web sources...")
    now_ts = datetime.strftime(datetime.now(), "%Y%m%d-%H%M%S")
    output_path = os.path.join("/home", "javi", "Projects", "products",  "dufur", "backend", "output", f"{now_ts}-data.json")
    logger.debug(output_path)
    # pdb.set_trace()
    try:
        data_dict = store_all_data(pages=pages)
        logger.debug(data_dict)
        logger.info("Data retrieved. Proceeding...")
    except Exception:
        logger.critical("Error fetching data from web sources")
        raise Exception
    if store_to_disk:
        logger.info("Saving data to disk...")
        try:
            store_in_file(data=data_dict, path_to_file=output_path)
            logger.info("Data stored. Proceeding...")
        except Exception:
            logger.critical("Error saving data to disk.")
            raise Exception
    return data_dict
