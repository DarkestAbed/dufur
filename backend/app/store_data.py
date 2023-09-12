import logging

from app.parse_dates import get_day_time_of_class


def store_data_in_dict(page: dict, availability: str) -> dict:
    from datetime import datetime
    from pprint import pprint
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
    pprint(inside_dict)
    return inside_dict
