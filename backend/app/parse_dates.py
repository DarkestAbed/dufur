import logging


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
    ## date_class_raw provides ddd-hhmm ; if provides ddd-hh, something must be done
    date_class_raw_opt_1 = url[idxs_slashes[3] + 1:idxs_dashes[1]]
    date_class_raw_opt_2 = url[idxs_slashes[3] + 1:idxs_dashes[2]]
    logging.debug(date_class_raw_opt_1)
    logging.debug(date_class_raw_opt_2)
    date_class_split = date_class_raw_opt_1.split("-")
    logging.debug(date_class_split)
    date_class = date_class_split[0]
    time_class_raw = date_class_split[1]
    logging.debug(len(date_class_split))
    if len(time_class_raw) == 4:
        time_class = f"{time_class_raw[0:2]}:{time_class_raw[2:]}"
    elif len(time_class_raw) < 4:
        date_class_split = date_class_raw_opt_2.split("-")
        time_class_raw = [date_class_split[1].strip(), date_class_split[2].strip().strip("hrs")]
        logging.debug(time_class_raw)
        time_class = f"{time_class_raw[0]}:{time_class_raw[1]}"
    else:
        raise Exception("Error fetching day and time of class")
    logging.debug(f"{date_class} {time_class}")
    return f"{date_class} {time_class}"
