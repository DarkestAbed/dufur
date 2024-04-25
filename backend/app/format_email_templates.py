# backend/app/format_email_templates.py
import os

from datetime import datetime
from jinja2 import Environment, FileSystemLoader

from backend.assets.config import DATE_FMT, LOGGING_LEVEL_CONSOLE
from shared.logger import Logger

logger = Logger(console_log_level=LOGGING_LEVEL_CONSOLE)


def load_templates(template_data: dict):
    # setup
    date_dt = datetime.strftime(datetime.now(), DATE_FMT)
    templates_loc = os.path.join(os.getcwd(), "backend", "templates")
    output_loc = os.path.join(os.getcwd(), "backend", "output", f"{date_dt}-email_template.html")
    logger.logger.debug(templates_loc)
    env = Environment(loader=FileSystemLoader(templates_loc))
    # template parsing
    template = env.get_template(name="child.html")
    logger.logger.debug(template_data)
    for item in template_data:
        logger.logger.debug(item)
    output = template.render(data=template_data)
    # template output
    with open(file=output_loc, mode="w") as file:
        file.write(output)
    return output_loc
