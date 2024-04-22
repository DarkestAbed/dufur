# backend_tasks.py

from backend.app.app_config import app_config
from backend.app.check_available_classes import class_check_orchestrator
from backend.app.parse_pages import parse_pages
from backend.app.store_data import store_process
from backend.app.send_email import email_process

from prefect import flow, task
from typing import Any


@task
def app_config():
    _: Any
    email: str
    _, email = app_config()
    return app_config

@task
def class_check():
    pass


@task
def parse_pages():
    pass


@task
def store():
    pass


@task
def send_emails():
    pass


@flow(log_prints=True)
def config_phase():
    pass


@flow(log_prints=True)
def scrapping():
    pass


@flow(log_prints=True)
def storage():
    pass


@flow(log_prints=True)
def workflow():
    pass