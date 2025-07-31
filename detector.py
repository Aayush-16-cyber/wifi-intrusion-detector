from scapy.all import ARP, Ether, srp
import time
import os
from datetime import datetime
import winsound

AUTHORIZED_FILE = "authorized_macs.txt"
LOG_FILE = "intruder_log.txt"
TARGET_SUBNET = "192.168.29.1/24"
BEEP_FREQUENCY = 1000  # Hz
BEEP_DURATION = 500    # ms


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_authorized_macs():
    if not os.path.exists(AUTHORIZED_FILE):
        open(AUTHORIZED_FILE, 'w').close()
    with open(AUTHORIZED_FILE, 'r') as f:
        return [line.strip().upper() for line in f.readlines()]


def add_authorized_mac(mac):
    with open(AUTHORIZED_FILE, 'a') as f:
        f.write(mac + '\n')
    print(f"✅ Added {mac} to authorized list.\n")


def log_intruder(ip, mac):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] INTRUDER: {ip} | {mac}\n")


def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for _, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc.upper()})
    return devices


def detect_intruders(devices, authorized_macs):
    print("🔍 Scanned Devices:\n" + "-" * 60)
    for device in devices:
        ip = device['ip']
        mac = device['mac']
        if mac in authorized_macs:
            print(f"✅ [AUTHORIZED]  {ip}  |  {mac}")
        else:
            print(f"⚠️  [INTRUDER]    {ip}  |  {mac}")
            winsound.Beep(BEEP_FREQUENCY, BEEP_DURATION)
            log_intruder(ip, mac)
            
            # ❗ Ask for each intruder individually
            try:
                choice = input("❓ Press 'A' to authorize this MAC, or Enter to skip: ").strip().lower()
                if choice == 'a':
                    add_authorized_mac(mac)
                    authorized_macs.append(mac)
            except:
                print("❌ Skipped adding.")
    print("-" * 60)


def main():
    print("🔐 Wi-Fi Intrusion Detector - Advanced Mode")
    print(f"🎯 Target Subnet: {TARGET_SUBNET}")
    print("📡 Scanning every 30 seconds...\n")

    while True:
        clear_console()
        authorized_macs = load_authorized_macs()
        print("🔄 Scanning for connected devices...\n")
        devices = scan_network(TARGET_SUBNET)
        detect_intruders(devices, authorized_macs)
        time.sleep(30)


if __name__ == "__main__":
    main()
