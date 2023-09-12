from app.parse_pages import get_pages_from_json, parse_pages


def main():
    dict_pages = get_pages_from_json()
    parse_pages(pages_dict=dict_pages)



if __name__ == "__main__":
    main()
else:
    pass
