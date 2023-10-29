import logging
import os

from datetime import datetime
from assets.config import LOGGING_LEVEL_CONSOLE, LOGGING_LEVEL_FILE, LOGGING_FORMAT, DATETIME_FMT


# logging config
## logger
date = datetime.strftime(datetime.now(), DATETIME_FMT)
logger = logging.getLogger("console_output")
## console logger
console_log = logging.StreamHandler()
## file logger
log_path = os.path.join(os.getcwd(), "output", f"{date}-execution.log")
file_log = logging.FileHandler(filename=log_path, mode="w", encoding="latin-1", delay=False)
## set levels
logger.setLevel(logging.DEBUG)
console_log.setLevel(LOGGING_LEVEL_CONSOLE)
file_log.setLevel(LOGGING_LEVEL_FILE)
## set up formatter
formatter = logging.Formatter(LOGGING_FORMAT)
console_log.setFormatter(formatter)
file_log.setFormatter(formatter)
## add console log to handler
logger.addHandler(console_log)
logger.addHandler(file_log)
