# orchestrator/tasks/backend_tasks.py
import os
import sys

sys.path.insert(0, f"{os.getcwd()}")

from backend.app.app_config import app_config
from backend.app.check_available_classes import class_check_orchestrator
from backend.app.parse_pages import parse_pages
from backend.app.store_data import store_process
from backend.app.send_email import email_process
from orchestrator.lib.doppler import doppler_login

from prefect import flow, task
from typing import Any, NoReturn


@task(retries=1)
def app_configuration() -> dict:
    _: Any
    config: dict
    _, config = app_config()
    return config

@task
def class_check() -> None:
    class_check_orchestrator()
    return None


@task
def parse_pages_yaml() -> dict:
    dict_pages: dict[str, str] = parse_pages(pages_loc=None)
    return dict_pages


@task
def store(dict_pages: dict[int, str]) -> dict:
    dict_data: dict[int, str] = store_process(pages=dict_pages)
    return dict_data


@task
def send_emails(dict_data: dict, email_vars: dict) -> None:
    email_process(data=dict_data, dict_config=email_vars)
    return None


@flow(log_prints=True)
def workflow() -> NoReturn:
    doppler_login()
    email_vars: dict = app_configuration()
    class_check()
    pages: dict = parse_pages_yaml()
    dict_data: dict = store(dict_pages=pages)
    send_emails(dict_data=dict_data, email_vars=email_vars)
    return None


if __name__ == "__main__":
    workflow()
else:
    pass
