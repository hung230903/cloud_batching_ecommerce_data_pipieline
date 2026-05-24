import IP2Location

from config.base import IP2LOCATION_DB

# Global IP2Location instance for worker processes
_ip2loc = None


def lookup_ip(ip):
    # This function is designed to be used in linux multiprocessing
    global _ip2loc
    if _ip2loc is None:
        # Initialize single instance for each worker process
        _ip2loc = IP2Location.IP2Location(IP2LOCATION_DB)

    record = _ip2loc.get_all(ip)

    return {
        "ip": ip,
        "country_short": record.country_short,
        "country": record.country_long,
        "region": record.region,
        "city": record.city,
    }
