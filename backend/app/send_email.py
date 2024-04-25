from typing import Union

from backend.app.format_email_templates import load_templates
from backend.lib.logger import Logger

logger = Logger()


def email_send(htmlfile_path: str, me: str, you: Union[list, str], password: str) -> None:
    # import pdb
    import smtplib
    from datetime import datetime
    from email.mime.text import MIMEText
    logger.debug(f"TEST CONFIG :: me: {me} ; you: {you} ")
    # pdb.set_trace()
    now_dt: str = datetime.strftime(datetime.now(), "%Y-%m-%d")
    logger.info("Sending data over email...")
    # hmtlfile is the email body
    with open(htmlfile_path, "r") as fp:
        msg: MIMEText = MIMEText(fp.read(), "html")
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


def email_process(data: dict, dict_config: dict) -> None:
    # import pdb
    # logger.info("Retrieving configurations for email send process...")
    # try:
    #     dict_config = load_vars(yaml_loc=None)
    #     logger.info("Config done. Proceeding...")
    #     # pdb.set_trace()
    # except Exception:
    #     logger.critical("Error while getting config vars for email process")
    #     raise Exception
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
