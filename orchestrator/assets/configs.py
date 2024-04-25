# orchestrator/assets/configs.py
import os

from logging import DEBUG, INFO

from shared.configs import BASE_PROJECT_PATH


# paths
BASE_ORCHESTRATOR_PATH = os.path.join(BASE_PROJECT_PATH, "orchestrator")
TOKEN_PATH = os.path.join(BASE_ORCHESTRATOR_PATH, "assets", "key.sct")
# secrets
PROJECT_NAME = "dufur"
SECRETS_ENV = "prd"
SECRETS_VARS = "EMAILS_ME,EMAILS_YOU,EMAILS_APP_PASSWORD,DOPPLER_ENVIRONMENT"
# logging
LOGGING_LVL_CONSOLE = INFO
LOGGING_LVL_FILE = INFO
