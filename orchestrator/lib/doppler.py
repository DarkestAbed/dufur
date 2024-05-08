# orchestrator/lib/doppler.py
from dopplersdk import DopplerSDK
from os import environ

from orchestrator.assets.configs import SECRETS_ENV, PROJECT_NAME, SECRETS_VARS
from orchestrator.lib.get_token import get_token
from orchestrator.lib.exceptions import UnableToRetrieveSecrets
from shared.logger import Logger

logger: Logger = Logger()


def doppler_login():
    from pprint import pprint
    logger.logger.info("Logging in to Doppler...")
    doppler: DopplerSDK = DopplerSDK()
    logger.logger.info(f"Requesting access for {SECRETS_ENV} environment...")
    try:
        access_token: str = get_token()
    except Exception as e:
        logger.logger.exception(f"Error getting access token. Exception found is {e}")
    logger.logger.debug(access_token)
    doppler.set_access_token(access_token)
    logger.logger.info("Getting secrets...")
    try:
        secrets_all: dict = vars(
            doppler.secrets.list(
                project=PROJECT_NAME,
                config=SECRETS_ENV,
                secrets=SECRETS_VARS,
                include_managed_secrets=False
            )
        )
    except Exception as e:
        logger.logger.exception(f"Error accessing secrets. Exception found is {e}")
        raise UnableToRetrieveSecrets
    secrets: dict = secrets_all["secrets"]
    for secret in secrets:
        environ[secret] = secrets[secret]["computed"]
    logger.logger.info("Loading env vars from Doppler...")
    exec_vars: str = environ.get("DOPPLER_ENVIRONMENT", None)
    email_vars: dict[str, str] = {
        "me": environ.get("EMAILS_ME", None),
        "you": environ.get("EMAILS_YOU", None),
        "app_password": environ.get("EMAILS_APP_PASSWORD", None),
    }
    return_tuple: tuple[dict, dict] = (exec_vars, email_vars)
    logger.logger.debug(return_tuple)
    # pdb.set_trace()
    logger.logger.info("App set up. Proceeding...")
    # pdb.set_trace()
    return return_tuple
