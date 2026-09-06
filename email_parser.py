from email import policy
from email.parser import BytesParser


def parse_email(file_path):

    with open(file_path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    # Keep headers as a dictionary for the rest of the application
    headers = {}

    for key, value in msg.items():

        # Preserve multiple headers such as Received
        if key in headers:

            if isinstance(headers[key], list):
                headers[key].append(str(value))
            else:
                headers[key] = [
                    headers[key],
                    str(value)
                ]

        else:
            headers[key] = str(value)

    # Create a complete searchable header string
    headers_text = ""

    for key, value in headers.items():

        if isinstance(value, list):

            for item in value:
                headers_text += f"{key}: {item}\n"

        else:
            headers_text += f"{key}: {value}\n"

    # Extract body
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
        "headers_text": headers_text,
        "body": body,
        "subject": msg.get("Subject", ""),
        "from": msg.get("From", ""),
        "to": msg.get("To", ""),
        "reply_to": msg.get("Reply-To", ""),
        "return_path": msg.get("Return-Path", "")
    }