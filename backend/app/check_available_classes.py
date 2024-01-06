from lib.url_crawler import Crawler
from lib.logger import Logger
from assets.config import BASE_URL, COURSES_JSON

logger = Logger()


def retrieve_all_product_links() -> list:
    # import pdb
    # from pprint import pprint
    crawler = Crawler(urls=[BASE_URL])
    crawler.run()
    urls = crawler.yield_urls()
    # for url in urls:
        # logger.debug(url)
        # pdb.set_trace()
    # pprint(urls)
    return urls


def validate_product_links(prod_list: list) -> list:
    # import pdb
    valid_days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
    list_return = []
    for product in prod_list:
        text_unparsed = product.strip()
        logger.debug(f"Text to parse: {product}")
        if text_unparsed[-1] == "/":
            text_split = text_unparsed.split("/")[-2]
        else:
            text_split = text_unparsed.split("/")[-1]
        logger.debug(f"Last piece of URL: {text_split}")
        text_split = text_split.split("-")[0]
        logger.debug(f"First piece of text: {text_split}")
        # pdb.set_trace()
        if text_split in valid_days:
            logger.debug("Valid class URL!")
            list_return.append(product)
    return list_return


def create_new_class_json_file(valid_prods: list) -> dict:
    dict_return = {
        "lunes": [],
        "martes": [],
        "miercoles": [],
        "jueves": [],
        "viernes": [],
        "sabado": [],
    }
    for prod in valid_prods:
        logger.debug(f"URL to process: {prod}")
        text_unparsed = prod.strip()
        if text_unparsed[-1] == "/":
            text_split = text_unparsed.split("/")[-2]
        else:
            text_split = text_unparsed.split("/")[-1]
        text_split = text_split.split("-")[0]
        logger.debug(f"Key: {text_split}")
        curr_list = dict_return.get(text_split, [])
        logger.debug(type(curr_list))
        logger.debug(f"Current dict key '{text_split}' : {curr_list}")
        curr_list.append(prod)
        logger.debug(curr_list)
        dict_return[text_split] = curr_list
        logger.debug(f"After appending, current dict key '{text_split}' : {curr_list}")
    return dict_return


def save_classes_to_json(courses_dict: dict) -> None:
    import json
    with open(file=COURSES_JSON, mode="w") as f:
        json.dump(obj=courses_dict, fp=f)
    return None


def class_check_orchestrator() -> None:
    import pdb
    from pprint import pprint
    products = retrieve_all_product_links()
    valid_products = validate_product_links(prod_list=products)
    pprint(valid_products)
    new_json = create_new_class_json_file(valid_prods=valid_products)
    pprint(new_json)
    save_classes_to_json(courses_dict=new_json)
    # pdb.set_trace()
    return None
