from lib.load_env_vars import load_vars
from lib.logger import Logger

logger = Logger()


def app_config() -> tuple:
    import pdb
    from os import environ
    logger.info("Setting up the app...")
    # check if doppler vars exist
    doppler_config: str = environ.get("DOPPLER_CONFIG", None)
    if doppler_config:
        logger.debug(f"{doppler_config = }")
        exec_vars: str = environ.get("DOPPLER_ENVIRONMENT", None)
        email_vars: dict[str, str] = {
            "me": environ.get("EMAILS_ME", None),
            "you": environ.get("EMAILS_YOU", None),
            "app_password": environ.get("EMAILS_APP_PASSWORD", None),
        }
    else:
        # load env variables
        env_dict: dict[str, str] = load_vars(yaml_loc=None)
        # define two var sets: exec and email
        email_vars: dict[str, str] = {
            "me": env_dict["me"],
            "you": env_dict["you"],
            "app_password": env_dict["app_password"],
        }
        exec_vars: dict[str, str] = {
            "loc": env_dict["loc"],
            "env": env_dict["env"],
        }
        # return tuple
    return_tuple: tuple[dict, dict] = (exec_vars, email_vars)
    logger.debug(return_tuple)
    # pdb.set_trace()
    logger.info("App set up. Proceeding...")
    # pdb.set_trace()
    return return_tuple