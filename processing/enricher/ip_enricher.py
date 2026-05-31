import threading
import IP2Location

from config.base import IP2LOCATION_DB

# Thread-local storage to maintain a separate IP2Location instance per thread
_thread_local = threading.local()


def get_ip2loc():
    if not hasattr(_thread_local, "instance"):
        _thread_local.instance = IP2Location.IP2Location(IP2LOCATION_DB)
    return _thread_local.instance


def lookup_ip(ip):
    # This function is now thread-safe
    db = get_ip2loc()
    record = db.get_all(ip)

    return {
        "ip": ip,
        "country_short": record.country_short,
        "country": record.country_long,
        "region": record.region,
        "city": record.city,
    }
