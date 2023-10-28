import logging

from app.parse_pages import retrieve_page
from app.load_html import load_html_page, fetch_stock_item
from app.parse_dates import get_day_time_of_class


def store_data_in_dict(page: dict, availability: str) -> dict:
    from datetime import datetime
    # from pprint import pprint
    now_fmt = "%Y-%m-%d %H:%M:%S.%f"
    now_ts = datetime.strftime(datetime.now(), now_fmt)
    logging.debug(now_ts)
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
    from pprint import pprint
    logging.debug(pages)
    full_dict = {}
    for index in range(0, len(pages)):
        page = retrieve_page(pages_dict=pages, idx=index)
        logging.debug(page)
        logging.debug(f"{index + 1} : {page}")
        try:
            soup = load_html_page(page)
        except Exception as e:
            msg = f"Encontramos un error al buscar las clases, para la clase {page[0]}, URL {page[1]}"
            logging.error(msg=msg)
            next
        cupos_disponibles = fetch_stock_item(soup=soup)
        temp_data = store_data_in_dict(page=page, availability=cupos_disponibles)
        logging.debug(f"Cupos disponibles? : {temp_data.get('category')} ({temp_data.get('date_class')}) :: {temp_data.get('availability')}")
        full_dict[index] = temp_data
    # pprint(full_dict)
    return full_dict


def store_in_file(data: dict, path_to_file: str) -> None:
    import json
    try:
        with open(path_to_file, "w") as file:
            json.dump(obj=data, fp=file)
    except Exception as e:
        logging.critical(f"Error saving classes data.\nException raised was {e}")
        raise Exception("Error saving classes data")
    return None


def store_process(pages: dict) -> dict:
    import os
    # import pdb
    from datetime import datetime
    logging.info("Fetching data from web sources...")
    now_ts = datetime.strftime(datetime.now(), "%Y%m%d-%H%M%S")
    output_path = os.path.join("/home", "javi", "Projects", "dufur", "backend", "output", f"{now_ts}-data.json")
    logging.debug(output_path)
    # pdb.set_trace()
    try:
        data_dict = store_all_data(pages=pages)
        logging.info("Data retrieved. Proceeding...")
    except Exception:
        logging.critical("Error fetching data from web sources")
        raise Exception
    logging.info("Saving data to disk...")
    try:
        store_in_file(data=data_dict, path_to_file=output_path)
        logging.info("Data stored. Proceeding...")
    except Exception:
        logging.critical("Error saving data to disk.")
        raise Exception
    return data_dict
