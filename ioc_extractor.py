import re
import ipaddress


def extract_ips(text):

    if not isinstance(text, str):
        return []

    candidates = re.findall(
        r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        text
    )

    valid_ips = []

    for ip in candidates:

        try:
            ipaddress.ip_address(ip)

            if ip not in valid_ips:
                valid_ips.append(ip)

        except ValueError:
            pass

    return valid_ips


def extract_urls(text):

    if not isinstance(text, str):
        return []

    urls = re.findall(
        r'https?://[^\s<>"\']+',
        text
    )

    return list(dict.fromkeys(urls))