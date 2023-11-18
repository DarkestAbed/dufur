from typing import Union
from app.format_email_templates import load_templates
from assets.config import RUN_ENV
from lib.exceptions import WrongExecutionEnvironment
from lib.logging_config import logger


def get_yaml_vars_email(yaml_loc: str = None) -> dict:
    # from pprint import pprint
    import os
    # import pdb
    import yaml
    if yaml_loc is None:
        if RUN_ENV == "local":
            CONFIG_FILE = "config_vars-dev.yml"
        elif RUN_ENV == "remote":
            CONFIG_FILE = "config_vars.yml"
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


def email_send(htmlfile_path: str, me: str, you: Union[list, str], password: str) -> None:
    # import pdb
    import smtplib
    from datetime import datetime
    from email.mime.text import MIMEText
    logger.debug(f"TEST CONFIG :: me: {me} ; you: {you} ")
    # pdb.set_trace()
    now_dt = datetime.strftime(datetime.now(), "%Y-%m-%d")
    logger.info("Sending data over email...")
    # TODO: refactor message contents
    # hmtlfile is the email body
    with open(htmlfile_path, "r") as fp:
        msg = MIMEText(fp.read(), "html")
    # TODO: end refactor piece
    msg["Subject"] = f"Clases y cupos, revisadas el {now_dt}"
    # me is sender email address
    # you is recipient email address
    msg["From"] = me
    if isinstance(you, list):
        msg["To"] = ",".join(you)
    elif isinstance(you, str):
        msg["To"] = you
    else:
        logger.critical("Wrong type of recipient")
        raise Exception
    # send email through smtp server
    with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465) as s:
        logger.info("Attempting email login...")
        s.login(user=me, password=password)
        logger.info("Attempting to send email...")
        if isinstance(you, list):
            s.sendmail(me, you, msg.as_string())
        elif isinstance(you, str):
            s.sendmail(me, [you], msg.as_string())
        else:
            logger.critical("Wrong type of recipient")
            raise Exception
    return None


def email_process(data: dict, yaml_loc: str = None) -> None:
    import pdb
    logger.info("Retrieving configurations for email send process...")
    try:
        dict_config = get_yaml_vars_email(yaml_loc=None)
        logger.info("Config done. Proceeding...")
        # pdb.set_trace()
    except Exception:
        logger.critical("Error while getting config vars for email process")
        raise Exception
    logger.info("Configuring email body message...")
    try:
        path = load_templates(template_data=data)
        logger.info("Message set up. Proceeding...")
    except Exception:
        logger.critical("Error configuring the message body")
        raise Exception
    # pdb.set_trace()
    logger.info("Sending email...")
    try:
        email_send(htmlfile_path=path, me=dict_config["me"], you=dict_config["you"], password=dict_config["app_password"])
        logger.info("Email sent. Proceeding...")
    except Exception:
        logger.critical("Error sending email")
        raise Exception
    return None
