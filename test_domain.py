from domain_analyzer import get_dns_records


domain = "example.com"

records = get_dns_records(domain)

print("DNS Records for:", domain)

print("\nA Records:")
print(records["A"])

print("\nMX Records:")
print(records["MX"])

print("\nNS Records:")
print(records["NS"])