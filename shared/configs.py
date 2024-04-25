# shared/configs.py
import os

from logging import DEBUG, INFO

# paths
BASE_PROJECT_PATH = os.getcwd()
# logginf
LOGGING_FORMAT = "%(asctime)s || %(filename)s::%(module)s - %(funcName)s (%(lineno)d) || %(process)d::%(processName)s :: %(levelname)s :: %(message)s"
LOGGING_LEVEL_CONSOLE = INFO
LOGGING_LEVEL_FILE = INFO
LOGGING_LEVEL_LOGGER = INFO
# formats
DATETIME_FMT = "%Y%m%d-%H%M%S"
TIMESTAMP_FMT = "%Y-%m-%d %H:%M:%S"
DATE_FMT = "%Y%m%d"
