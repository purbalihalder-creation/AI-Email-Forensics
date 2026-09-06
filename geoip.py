import ipaddress
import requests


def geolocate_ip(ip):
    """
    Get approximate geolocation information for a public IP.
    """

    result = {
        "IP": ip,
        "City": "Unknown",
        "Region": "Unknown",
        "Country": "Unknown",
        "ISP": "Unknown",
        "Latitude": None,
        "Longitude": None
    }

    try:
        ip_obj = ipaddress.ip_address(ip)

        # Private IP
        if ip_obj.is_private:
            result.update({
                "City": "Private Network",
                "Region": "N/A",
                "Country": "N/A",
                "ISP": "Private IP"
            })
            return result

        # Reserved / documentation IP
        if ip_obj.is_reserved:
            result.update({
                "City": "Reserved/Test IP",
                "Region": "N/A",
                "Country": "N/A",
                "ISP": "Documentation Address"
            })
            return result

        # ipwho.is API
        url = f"https://ipwho.is/{ip}"

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "AI-Email-Forensics/1.0"
            }
        )

        print("Geolocation URL:", url)
        print("HTTP Status:", response.status_code)

        response.raise_for_status()

        data = response.json()

        if not data.get("success", False):
            print("Geolocation API error:", data)
            result["City"] = "Lookup Failed"
            return result

        connection = data.get("connection", {})

        result.update({
            "City": data.get("city") or "Unknown",
            "Region": data.get("region") or "Unknown",
            "Country": data.get("country") or "Unknown",
            "ISP": connection.get("isp") or "Unknown",
            "Latitude": data.get("latitude"),
            "Longitude": data.get("longitude")
        })

        return result

    except requests.exceptions.RequestException as e:

        print("Network/API error:", e)
        result["City"] = "API Error"
        return result

    except Exception as e:

        print("Geolocation error:", e)
        result["City"] = "Lookup Error"
        return result