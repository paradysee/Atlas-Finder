import requests

def run(ip: str):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=10).json()

        if r.get("status") != "success":
            return None

        return {
            "IP": ip,
            "Country": r.get("country"),
            "Region": r.get("regionName"),
            "City": r.get("city"),
            "ISP": r.get("isp"),
            "ASN": r.get("as"),
            "Lat/Lon": f"{r.get('lat')} / {r.get('lon')}"
        }

    except Exception:
        return None

