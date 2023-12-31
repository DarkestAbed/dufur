import os

from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from assets.config import DATE_FMT
from lib.logger import Logger

logger = Logger()


def load_templates(template_data: dict):
    # setup
    date_dt = datetime.strftime(datetime.now(), DATE_FMT)
    templates_loc = os.path.join(os.getcwd(), "templates")
    output_loc = os.path.join(os.getcwd(), "output", f"{date_dt}-email_template.html")
    logger.debug(templates_loc)
    env = Environment(loader=FileSystemLoader(templates_loc))
    # template parsing
    template = env.get_template(name="child.html")
    logger.debug(template_data)
    for item in template_data:
        logger.debug(item)
    output = template.render(data=template_data)
    # template output
    with open(file=output_loc, mode="w") as file:
        file.write(output)
    return output_loc
