from email_parser import parse_email
from ioc_extractor import extract_ips

email_data = parse_email(
    "sample_emails/phishing_sample.eml"
)

print("\n===== HEADERS =====")
print(email_data["headers_text"])

print("\n===== EXTRACTED IPs =====")

ips = extract_ips(email_data["headers_text"])

for ip in ips:
    print(ip)