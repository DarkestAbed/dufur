from typing import Union
from app.format_email_templates import load_templates
from lib.logging_config import logger


def get_yaml_vars_email(yaml_loc: str = None) -> dict:
    # from pprint import pprint
    import os
    # import pdb
    import yaml
    if yaml_loc is None:
        yaml_loc = os.path.join(os.getcwd(), "assets", "config_vars.yml")
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


def build_email_message(data: dict) -> str:
    import os
    from datetime import datetime
    # from pprint import pprint
    # build message
    # pprint(data)
    messages = []
    init_msg = "Hola! Acá van las disponibilidades de todas las clases de la academia Natalia Dufuur:\n\n"
    messages.append(init_msg)
    for idx in data:
        # pprint(data[idx])
        _dict = data[idx]
        if not _dict.get("availability") == "Agotado":
            line_msg = f"> La clase {_dict.get('category')}, del {_dict.get('date_class')} hrs., tiene estos cupos: {_dict.get('availability')}\n"
        else:
            line_msg = f"> La clase {_dict.get('category')}, del {_dict.get('date_class')} hrs., no tiene cupos disponibles :(\n"
        line_msg += f"Esta es la página de la clase: {_dict.get('url')}"
        logger.debug(line_msg)
        messages.append(line_msg)
    eol_msg = f"Revisé en esta fecha: {data[len(data)-1].get('check_time')}\n\nBesis! Bai!"
    messages.append(eol_msg)
    body_msg = "\n\n===\n\n".join(messages)
    # build message file path
    now_ts = datetime.strftime(datetime.now(), "%Y%m%d-%H%M%S")
    output_path = os.path.join(os.getcwd(), "output", f"{now_ts}-message.txt")
    logger.debug(output_path)
    # pprint(messages)
    logger.debug(body_msg)
    # write message to text
    with open(file=output_path, mode="w") as msg:
        msg.write(body_msg)
    return output_path


def email_send(textfile_path: str, me: str, you: Union[list, str], password: str) -> None:
    # import pdb
    import smtplib
    from datetime import datetime
    from email.mime.text import MIMEText
    logger.debug(f"TEST CONFIG :: me: {me} ; you: {you} ")
    # pdb.set_trace()
    now_dt = datetime.strftime(datetime.now(), "%Y-%m-%d")
    logger.info("Sending data over email...")
    # TODO: refactor message contents
    # textfile is the message content file
    with open(textfile_path, "r") as fp:
        msg = MIMEText(fp.read(), "plain")
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
        logger.debug(load_templates(template_data=data))
        logger.info("Config done. Proceeding...")
        pdb.set_trace()
    except Exception:
        logger.critical("Error while getting config vars for email process")
        raise Exception
    logger.info("Configuring email body message...")
    try:
        path = build_email_message(data=data)
        logger.info("Message set up. Proceeding...")
    except Exception:
        logger.critical("Error configuring the message body")
        raise Exception
    # pdb.set_trace()
    logger.info("Sending email...")
    try:
        email_send(textfile_path=path, me=dict_config["me"], you=dict_config["you"], password=dict_config["app_password"])
        logger.info("Email sent. Proceeding...")
    except Exception:
        logger.critical("Error sending email")
        raise Exception
    return None
