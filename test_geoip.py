from geoip import geolocate_ip

test_ips = [
    "8.8.8.8",
    "1.1.1.1"
]

for ip in test_ips:

    result = geolocate_ip(ip)

    print("\nIP:", ip)
    print("City:", result["City"])
    print("Region:", result["Region"])
    print("Country:", result["Country"])
    print("ISP:", result["ISP"])
    print("Latitude:", result["Latitude"])
    print("Longitude:", result["Longitude"])