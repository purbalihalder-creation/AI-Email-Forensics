from email_parser import parse_email

data = parse_email("sample_emails/phishing_sample.eml")

print("Subject:", data["subject"])
print("From:", data["from"])
print("To:", data["to"])
print("Reply-To:", data["reply_to"])
print("\nBODY:")
print(data["body"])