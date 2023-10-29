from app.parse_pages import parse_pages
from app.store_data import store_process
from app.send_email import email_process


def main():
    dict_pages = parse_pages(pages_loc=None)
    dict_data = store_process(pages=dict_pages)
    email_process(data=dict_data, yaml_loc=None)


if __name__ == "__main__":
    main()
else:
    pass
