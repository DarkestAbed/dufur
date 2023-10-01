import logging


def build_email_message(textfile_path: str, data: dict) -> None:
    pass


def email_send(textfile_path: str, me: str, you: str) -> None:
    # imports
    import smtplib
    from email.mime.text import MIMEText
    # exec
    logging.info("Sending data over email...")
    # textfile is the message content file
    with open(textfile_path, "rb") as fp:
        msg = MIMEText(fp.read())
    msg["Subject"] = f"The contents of {textfile_path}"
    # me is sender email address
    # you is recipient email address
    msg["From"] = me
    msg["To"] = you
    # send email through smtp server
    s = smtplib.SMTP("localhost")
    s.sendmail(me, [you], msg.as_string())
    s.quit()
    logging.info("Email sent. Proceeding...")
    # wrap up
    return None
