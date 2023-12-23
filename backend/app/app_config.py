from lib.load_env_vars import load_vars
from lib.logger import Logger

logger = Logger()


def app_config() -> tuple:
    # import pdb
    logger.info("Setting up the app...")
    # load env variables
    env_dict = load_vars(yaml_loc=None)
    # define two var sets: exec and email
    email_vars = {
        "me": env_dict["me"],
        "you": env_dict["you"],
        "app_password": env_dict["app_password"],
    }
    exec_vars = {
        "loc": env_dict["loc"],
        "env": env_dict["env"],
    }
    # return tuple
    return_tuple = (exec_vars, email_vars)
    logger.debug(return_tuple)
    logger.info("App set up. Proceeding...")
    # pdb.set_trace()
    return return_tuple