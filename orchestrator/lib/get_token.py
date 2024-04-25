# orchestrator/lib/get_token.py
import os

from orchestrator.assets.configs import TOKEN_PATH, LOGGING_LVL_CONSOLE
from shared.logger import Logger

logger: Logger = Logger(console_log_level=LOGGING_LVL_CONSOLE)


def get_token() -> str:
    if os.path.exists(TOKEN_PATH):
        logger.logger.info("Reading file...")
        with open(file=TOKEN_PATH, mode="r", encoding="utf-8") as tk:
            token: str = tk.read().strip()
            logger.logger.debug(token)
            if token is None or token.strip() == "":
                raise ValueError("Token file empty")
            else:
                return token
    else:
        raise FileNotFoundError("Token file not found")
