import re
from urllib.parse import urlparse


IP_REGEX = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"


def extract_ips(headers):

    text = ""

    for key, value in headers.items():

        if key.lower() == "received":
            text += str(value) + "\n"

    ips = re.findall(IP_REGEX, text)

    return list(dict.fromkeys(ips))


def extract_urls(body):

    url_regex = r'https?://[^\s<>"\']+'

    urls = re.findall(url_regex, body)

    return list(dict.fromkeys(urls))


def extract_domains(urls):

    domains = []

    for url in urls:

        try:

            parsed = urlparse(url)

            if parsed.hostname:
                domains.append(parsed.hostname)

        except Exception:
            pass

    return list(dict.fromkeys(domains))