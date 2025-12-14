from pywifi import PyWiFi, const, Profile
import time

def scan_networks():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(3)
    results = iface.scan_results()

    networks = []
    seen_ssids = set()
    for network in results:
        if network.ssid and network.ssid not in seen_ssids:
            seen_ssids.add(network.ssid)
            networks.append(network.ssid)
    return networks

def connect_to_network(ssid: str, password: str) -> bool:
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]

    iface.disconnect()
    time.sleep(1)

    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)

    iface.connect(tmp_profile)
    time.sleep(10)

    return iface.status() == const.IFACE_CONNECTED
