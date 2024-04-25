# backend/app/store_data.py
from backend.app.parse_pages import retrieve_page
from backend.app.load_html import load_html_page, fetch_stock_item, fetch_class_name
from backend.app.parse_values import get_day_time_of_class, get_class_title
from backend.assets.config import TIMESTAMP_FMT, LOGGING_LEVEL_CONSOLE
from shared.logger import Logger

logger: Logger = Logger(console_log_level=LOGGING_LEVEL_CONSOLE)


def store_data_in_dict(page: dict, class_title: str, availability: str) -> dict:
    import pdb
    from datetime import datetime
    # from pprint import pprint
    now_ts = datetime.strftime(datetime.now(), TIMESTAMP_FMT)
    logger.logger.debug(now_ts)
    title_class = get_class_title(text=class_title)
    logger.logger.debug(title_class)
    date_class = get_day_time_of_class(url=page[1])
    logger.logger.debug(date_class)
    # pdb.set_trace()
    inside_dict = {
        "category": title_class.title(),
        "url": page[1],
        "date_class": date_class,
        "availability": availability,
        "check_time": now_ts,
    }
    # pprint(inside_dict)
    return inside_dict


def store_all_data(pages: dict) -> dict:
    import pdb
    # from pprint import pprint
    logger.logger.debug(pages)
    # pdb.set_trace()
    full_dict: dict = {}
    for index in range(0, len(pages)):
        page = retrieve_page(pages_dict=pages, idx=index)
        # logger.logger.debug(page)
        # pdb.set_trace()
        logger.logger.debug(f"{index + 1} : {page}")
        # pdb.set_trace()
        try:
            soup = load_html_page(page)
        except Exception as e:
            msg = f"Encontramos un error al buscar las clases, para la clase {page[0]}, URL {page[1]}"
            logger.logger.error(msg=msg)
            next
        clase = fetch_class_name(soup=soup)
        cupos_disponibles = fetch_stock_item(soup=soup)
        # pdb.set_trace()
        temp_data = store_data_in_dict(page=page, class_title=clase, availability=cupos_disponibles)
        logger.logger.debug(f"Cupos disponibles? : {temp_data.get('category')} ({temp_data.get('date_class')}) :: {temp_data.get('availability')}")
        full_dict[index] = temp_data
        # pdb.set_trace()
    # pprint(full_dict)
    return full_dict


def store_in_file(data: dict, path_to_file: str) -> None:
    import json
    try:
        with open(path_to_file, "w") as file:
            json.dump(obj=data, fp=file)
    except Exception as e:
        logger.logger.critical(f"Error saving classes data.\nException raised was {e}")
        raise Exception("Error saving classes data")
    return None


def store_process(pages: dict, store_to_disk: bool = True) -> dict:
    import os
    # import pdb
    from datetime import datetime
    logger.logger.info("Fetching data from web sources...")
    now_ts = datetime.strftime(datetime.now(), "%Y%m%d-%H%M%S")
    output_path = os.path.join("/home", "javi", "Projects", "dufur", "backend", "output", f"{now_ts}-data.json")
    logger.logger.debug(output_path)
    # pdb.set_trace()
    try:
        data_dict = store_all_data(pages=pages)
        logger.logger.debug(data_dict)
        logger.logger.info("Data retrieved. Proceeding...")
    except Exception:
        logger.logger.critical("Error fetching data from web sources")
        raise Exception
    if store_to_disk:
        logger.logger.info("Saving data to disk...")
        try:
            store_in_file(data=data_dict, path_to_file=output_path)
            logger.logger.info("Data stored. Proceeding...")
        except Exception:
            logger.logger.critical("Error saving data to disk.")
            raise Exception
    return data_dict
