from lib.logger import Logger

logger = Logger()


def find_occurrences(s, ch):
    """
    Source:
    https://stackoverflow.com/questions/13009675/find-all-the-occurrences-of-a-character-in-a-string
    """
    return [i for i, letter in enumerate(s) if letter == ch]


def get_day_time_of_class(url: str) -> str:
    # get the second index of a dash on the url string
    idxs_dashes = find_occurrences(s=url, ch="-")
    idxs_slashes = find_occurrences(s=url, ch="/")
    logger.debug(f"url: {url} ; dashes: {idxs_dashes} ; slashes: {idxs_slashes}")
    ## date_class_raw provides ddd-hhmm ; if provides ddd-hh, something must be done
    try:
        date_class_raw_opt_1 = url[idxs_slashes[3] + 1:idxs_dashes[1]]
    except IndexError:
        date_class_raw_opt_1 = None
    logger.debug(date_class_raw_opt_1)
    try:
        date_class_raw_opt_2 = url[idxs_slashes[3] + 1:idxs_dashes[2]]
    except IndexError:
        date_class_raw_opt_2 = date_class_raw_opt_1
    logger.debug(date_class_raw_opt_2)
    # trying something...
    date_class_split = date_class_raw_opt_1.split("-")
    logger.debug(date_class_split)
    date_class = date_class_split[0]
    time_class_raw = date_class_split[1]
    logger.debug(len(date_class_split))
    if len(time_class_raw) == 4:
        time_class = f"{time_class_raw[0:2]}:{time_class_raw[2:]}"
    elif len(time_class_raw) < 4:
        date_class_split = date_class_raw_opt_2.split("-")
        time_class_raw = [date_class_split[1].strip(), date_class_split[2].strip().strip("hrs")]
        logger.debug(time_class_raw)
        time_class = f"{time_class_raw[0]}:{time_class_raw[1]}"
    else:
        raise Exception("Error fetching day and time of class")
    logger.debug(f"{date_class} {time_class}")
    return f"{date_class} {time_class}"


def get_class_title(text: str) -> str:
    import pdb
    # strip the string of dots and colons. it'll be easier this way
    text_clean = text.replace(".", "").replace(":", "").lower()
    logger.debug(f"Probando texto: {text_clean}")
    # find the index of string "hrs"
    idx_hrs = text_clean.find("hrs")
    logger.debug(idx_hrs)
    logger.debug(text_clean[idx_hrs + 3:].strip())
    # pdb.set_trace()
    if idx_hrs > 0:
        class_title = text_clean[idx_hrs + 3:].strip()
    else:
        import re
        re_digits = re.search(r"\d", text_clean)
        idx_hrs = re_digits.start()
        class_title = text_clean[idx_hrs + 4:].strip()
    return class_title
