from email import policy
from email.parser import BytesParser


def parse_email(file_path):

    with open(file_path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    headers = {}

    for key, value in msg.items():
        headers[key] = value

    body = ""

    if msg.is_multipart():

        for part in msg.walk():

            content_type = part.get_content_type()

            if content_type == "text/plain":
                try:
                    body += part.get_content()
                except Exception:
                    pass

    else:

        try:
            body = msg.get_content()
        except Exception:
            body = ""

    return {
        "headers": headers,
        "body": body,
        "subject": msg.get("Subject", ""),
        "from": msg.get("From", ""),
        "to": msg.get("To", ""),
        "reply_to": msg.get("Reply-To", ""),
        "return_path": msg.get("Return-Path", "")
    }