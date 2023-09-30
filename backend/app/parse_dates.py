import logging


def find_occurrences(s, ch):
    """
    https://stackoverflow.com/questions/13009675/find-all-the-occurrences-of-a-character-in-a-string
    """
    return [i for i, letter in enumerate(s) if letter == ch]


def get_day_time_of_class(url: str) -> str:
    # get the second index of a dash on the url string
    idxs_dashes = find_occurrences(s=url, ch="-")
    idxs_slashes = find_occurrences(s=url, ch="/")
    date_class_raw = url[idxs_slashes[3] + 1:idxs_dashes[1]]
    logging.debug(date_class_raw)
    date_class_split = date_class_raw.split("-")
    logging.debug(date_class_split)
    date_class = date_class_split[0]
    time_class_raw = date_class_split[1]
    time_class = f"{time_class_raw[0:2]}:{time_class_raw[2:]}"
    logging.debug(time_class)
    return f"{date_class} {time_class}"
