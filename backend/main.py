from app.app_config import app_config
from app.parse_pages import parse_pages
from app.store_data import store_process
from app.send_email import email_process


def main():
    import pdb
    from pprint import pprint
    # check_classes_test()
    # pdb.set_trace()
    _, email_vars = app_config()
    dict_pages = parse_pages(pages_loc=None)
    pprint(dict_pages)
    # pdb.set_trace()
    dict_data = store_process(pages=dict_pages)
    email_process(data=dict_data, dict_config=email_vars)


if __name__ == "__main__":
    main()
else:
    pass
