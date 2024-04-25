import logging
import os

from datetime import datetime
from typing import Any

from shared.configs import LOGGING_LEVEL_LOGGER, LOGGING_LEVEL_CONSOLE, LOGGING_LEVEL_FILE, LOGGING_FORMAT, DATE_FMT, BASE_PROJECT_PATH


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        # NOTE: commented else block to enable true singleton and no re-init of the class
        # else:
        #     cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    def __init__(self, log_level: Any = LOGGING_LEVEL_LOGGER, file_log_level: Any = LOGGING_LEVEL_FILE, console_log_level: Any = LOGGING_LEVEL_CONSOLE) -> None:
        date = datetime.strftime(datetime.now(), DATE_FMT)
        self.logger = logging.getLogger(__name__)
        ## console logger
        self.console_log = logging.StreamHandler()
        ## file logger
        log_path = os.path.join(BASE_PROJECT_PATH, "logs", f"{date}-execution.log")
        self.file_log = logging.FileHandler(filename=log_path, mode="w", encoding="latin-1", delay=False)
        ## set levels
        self.logger.setLevel(level=log_level)
        self.console_log.setLevel(level=console_log_level)
        self.file_log.setLevel(level=file_log_level)
        ## set up formatter
        formatter = logging.Formatter(LOGGING_FORMAT)
        self.console_log.setFormatter(formatter)
        self.file_log.setFormatter(formatter)
        ## add logs to handler
        self.logger.addHandler(self.console_log)
        self.logger.addHandler(self.file_log)
        return None
