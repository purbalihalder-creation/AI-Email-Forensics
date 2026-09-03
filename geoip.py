import requests


def geolocate_ip(ip):

    url = f"http://ip-api.com/json/{ip}"

    try:

        response = requests.get(
            url,
            timeout=5
        )

        data = response.json()

        if data.get("status") == "success":

            return {
                "ip": ip,
                "country": data.get("country"),
                "region": data.get("regionName"),
                "city": data.get("city"),
                "isp": data.get("isp"),
                "org": data.get("org"),
                "as": data.get("as"),
                "lat": data.get("lat"),
                "lon": data.get("lon")
            }

    except Exception as e:

        return {
            "ip": ip,
            "error": str(e)
        }

    return {
        "ip": ip,
        "error": "Unable to geolocate"
    }