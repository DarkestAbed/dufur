from typing import Any

from app.app_config import app_config
from app.check_available_classes import class_check_orchestrator
from app.parse_pages import parse_pages
from app.store_data import store_process
from app.send_email import email_process


def main():
    import pdb
    from pprint import pprint
    _: Any
    email_vars: str
    _, email_vars = app_config()
    # pdb.set_trace()
    class_check_orchestrator()
    # pdb.set_trace()
    dict_pages: dict[str, str] = parse_pages(pages_loc=None)
    pprint(dict_pages)
    # pdb.set_trace()
    dict_data: dict[int, str] = store_process(pages=dict_pages)
    # pdb.set_trace()
    email_process(data=dict_data, dict_config=email_vars)


if __name__ == "__main__":
    main()
else:
    pass
