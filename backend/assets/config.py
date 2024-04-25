import os

from logging import INFO, DEBUG


# logginf
LOGGING_FORMAT = "%(asctime)s || %(filename)s::%(module)s - %(funcName)s || %(process)d::%(processName)s :: %(levelname)s :: %(message)s"
LOGGING_LEVEL_CONSOLE = DEBUG
LOGGING_LEVEL_FILE = DEBUG
LOGGING_LEVEL_LOGGER = DEBUG
# formats
DATETIME_FMT = "%Y%m%d-%H%M%S"
TIMESTAMP_FMT = "%Y-%m-%d %H:%M:%S"
DATE_FMT = "%Y%m%d"
# envs
RUN_ENV = "dev"
# physical routes
COURSES_JSON = os.path.join(os.getcwd(), "backend", "assets", "cursos.json")
BASE_URL = "https://nataliadufuur.com/clases-presenciales/"
