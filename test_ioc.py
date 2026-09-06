from ioc_extractor import extract_ips

sample = """
Received: from mail.example.net (mail.example.net [203.0.113.10])
by victim.example.com

Received: from unknown-host (unknown-host [185.220.101.10])
by mail.example.net
"""

ips = extract_ips(sample)

print("Extracted IPs:")
for ip in ips:
    print(ip)