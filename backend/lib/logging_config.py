import logging
import os

from datetime import datetime
from assets.config import LOGGING_LEVEL_LOGGER, LOGGING_LEVEL_CONSOLE, LOGGING_LEVEL_FILE, LOGGING_FORMAT, DATETIME_FMT


# NOTE: refactor of the logger method
class logger:
    def __init__(self) -> None:
        date = datetime.strftime(datetime.now(), DATETIME_FMT)
        self.logger = logging.getLogger("output")
        ## console logger
        self.console_log = logging.StreamHandler()
        ## file logger
        log_path = os.path.join(os.getcwd(), "output", f"{date}-execution.log")
        self.file_log = logging.FileHandler(filename=log_path, mode="w", encoding="latin-1", delay=False)
        ## set levels
        self.logger.setLevel(LOGGING_LEVEL_LOGGER)
        self.console_log.setLevel(LOGGING_LEVEL_CONSOLE)
        self.file_log.setLevel(LOGGING_LEVEL_FILE)
        ## set up formatter
        formatter = logging.Formatter(LOGGING_FORMAT)
        self.console_log.setFormatter(formatter)
        self.file_log.setFormatter(formatter)
        ## add logs to handler
        logger.addHandler(self.console_log)
        logger.addHandler(self.file_log)
        return None

    def debug(self, msg: str) -> None:
        self.logger.debug(msg=msg)
        return None

    def info(self, msg: str) -> None:
        self.logger.info(msg=msg)
        return None

    def warning(self, msg: str) -> None:
        self.logger.warning(msg=msg)
        return None

    def error(self, msg: str) -> None:
        self.logger.error(msg=msg)
        return None

    def critical(self, msg: str) -> None:
        self.logger.critical(msg=msg)
        return None

    def exception(self, msg: str, *args) -> None:
        self.logger.exception(msg=msg, args=args)
        return None
