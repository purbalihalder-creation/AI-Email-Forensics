import re


def analyze_headers(data):

    headers = data["headers"]

    result = {
        "spf": "unknown",
        "dkim": "unknown",
        "dmarc": "unknown",
        "received_headers": [],
        "message_id": headers.get("Message-ID", ""),
        "return_path": headers.get("Return-Path", ""),
        "reply_to": headers.get("Reply-To", "")
    }

    authentication = headers.get("Authentication-Results", "")

    authentication_lower = authentication.lower()

    if "spf=pass" in authentication_lower:
        result["spf"] = "pass"

    elif "spf=fail" in authentication_lower:
        result["spf"] = "fail"

    if "dkim=pass" in authentication_lower:
        result["dkim"] = "pass"

    elif "dkim=fail" in authentication_lower:
        result["dkim"] = "fail"

    if "dmarc=pass" in authentication_lower:
        result["dmarc"] = "pass"

    elif "dmarc=fail" in authentication_lower:
        result["dmarc"] = "fail"

    for key, value in headers.items():

        if key.lower() == "received":
            result["received_headers"].append(value)

    return result