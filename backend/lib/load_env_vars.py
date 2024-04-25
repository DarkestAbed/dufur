import os
import yaml

from backend.lib.exceptions import WrongExecutionEnvironment
from backend.lib.logger import Logger

logger = Logger()


def get_yaml_vars_email(env: str) -> dict:
    if env == "dev":
        CONFIG_FILE = "config_vars-email-dev.yml"
    elif env == "prod":
        CONFIG_FILE = "config_vars-email-prod.yml"
    else:
        raise WrongExecutionEnvironment
    yaml_loc = os.path.join(os.getcwd(), "assets", CONFIG_FILE)
    logger.debug(yaml_loc)
    logger.debug(os.path.exists(path=yaml_loc))
    if not os.path.exists(path=yaml_loc):
        raise Exception("No JSON file located")
    with open(file=yaml_loc, mode="r") as file:
        dict_yaml = yaml.safe_load(file)
    logger.debug(dict_yaml)
    # pprint(dict_yaml)
    # pdb.set_trace()
    logger.debug(dict_yaml[0].get("emails"))
    return dict_yaml[0].get("emails")


def get_yaml_vars_exec(yaml_loc: str = None) -> dict:
    # import pdb
    # from pprint import pprint
    from backend.assets.config import RUN_ENV
    if yaml_loc is None:
        CONFIG_FILE = "config_vars-exec.yml"
        yaml_loc = os.path.join(os.getcwd(), "backend", "assets", CONFIG_FILE)
        logger.debug(yaml_loc)
    logger.debug(os.path.exists(path=yaml_loc))
    if not os.path.exists(path=yaml_loc):
        raise Exception("No JSON file located")
    with open(file=yaml_loc, mode="r") as file:
        dict_yaml = yaml.safe_load(file)
    logger.debug(dict_yaml)
    return_dict = {
        "loc": dict_yaml[0].get("loc", None),
        "env": dict_yaml[1].get("env", None),
    }
    if return_dict.get("env", None) is None:
        return_dict["env"] == RUN_ENV
    # pprint(dict_yaml)
    # pdb.set_trace()
    return return_dict

def load_vars(yaml_loc: str = None) -> dict:
    # import pdb
    logger.info("Loading environment variables...")
    exec_vars = get_yaml_vars_exec(yaml_loc=None)
    email_vars = get_yaml_vars_email(env=exec_vars["env"])
    all_vars = {**exec_vars, **email_vars}
    logger.debug(all_vars)
    # pdb.set_trace()
    return all_vars
