# CyberSecurityInvestigator (CSI-Tool) v1.0
# Author: Sanusi Saminu (GitHub: https://github.com/Sanusi644)
# Email: saminu644@gmail.com
# Disclaimer: This tool is for legal cybersecurity forensics and device analysis only.

import os
from colorama import Fore, init

init(autoreset=True)

PRIVATE_KEY = "SydSanusi@CyberKey#2025"

def verify_key():
    os.system("cls" if os.name == "nt" else "clear")
    print("Cyber Security Investigation Tool")
    key = input("Enter your investigator key: ").strip()
    if key != PRIVATE_KEY:
        print("Access denied. Unauthorized use is prohibited.")
        print("Contact: saminu644@gmail.com for credentials.")
        exit()
    print("Access granted.")

def network_analysis():
    target = input("Enter IP or domain to scan: ").strip()
    os.system(f"nmap -Pn {target}")

def vulnerability_scanner():
    target = input("Enter domain (e.g. http://example.com): ").strip()
    os.system(f"curl -I {target}")

def log_analysis():
    log_file = input("Enter path to log file: ").strip()
    os.system(f"grep -Ei 'fail|invalid|denied' {log_file}")

def sql_injection_detector():
    url = input("Enter target URL with param (e.g., http://site.com/item?id=1): ").strip()
    payloads = ["' OR '1'='1", "'--", "' OR '1'='1' --", "') OR ('1'='1"]
    for payload in payloads:
        print(f"Testing payload: {payload}")
        os.system(f"curl "{url}{payload}"")

def sydsanusi_cracker():
    print("SydSanusiCracker - Educational Crypto Wallet Cracker")
    print("1. Bitcoin
2. Ethereum
3. Tron
4. BNB
5. Litecoin")
    wallet_type = input("Select wallet type: ").strip()
    wordlist_path = input("Enter dictionary path: ").strip()
    if not os.path.exists(wordlist_path):
        print("Wordlist file not found.")
        return
    with open(wordlist_path, 'r') as f:
        for line in f:
            mnemonic = line.strip()
            print(f"Trying mnemonic: {mnemonic}")
    print("Simulation complete.")

def phone_sploit_menu():
    while True:
        print("""
PhoneSploit ADB Toolkit
1. List devices        2. Connect via IP
3. Shell access        4. Pull file from device
5. Push file to device 6. Reboot device
7. Lock screen         8. Uninstall app
9. Screenshot         10. List installed apps
11. Launch app        12. Restart ADB
13. Clear app data    14. Disconnect
15. Enable Wi-Fi ADB  16. Screen record
17. Volume info       18. Battery status
19. Device info       20. Open settings
21. Exit to main
""")
        ch = input("Select option: ").strip()
        if ch == "1":
            os.system("adb devices")
        elif ch == "2":
            ip = input("IP: ")
            os.system(f"adb connect {ip}")
        elif ch == "3":
            os.system("adb shell")
        elif ch == "4":
            r = input("Remote path: ")
            l = input("Local path: ")
            os.system(f"adb pull {r} {l}")
        elif ch == "5":
            l = input("Local path: ")
            r = input("Remote path: ")
            os.system(f"adb push {l} {r}")
        elif ch == "6":
            os.system("adb reboot")
        elif ch == "7":
            os.system("adb shell input keyevent 26")
        elif ch == "8":
            pkg = input("Package: ")
            os.system(f"adb uninstall {pkg}")
        elif ch == "9":
            os.system("adb shell screencap -p /sdcard/screen.png")
            os.system("adb pull /sdcard/screen.png ./screenshot.png")
        elif ch == "10":
            os.system("adb shell pm list packages")
        elif ch == "11":
            pkg = input("Package: ")
            os.system(f"adb shell monkey -p {pkg} -c android.intent.category.LAUNCHER 1")
        elif ch == "12":
            os.system("adb kill-server && adb start-server")
        elif ch == "13":
            pkg = input("Package: ")
            os.system(f"adb shell pm clear {pkg}")
        elif ch == "14":
            os.system("adb disconnect")
        elif ch == "15":
            os.system("adb tcpip 5555")
        elif ch == "16":
            os.system("adb shell screenrecord /sdcard/demo.mp4")
            os.system("adb pull /sdcard/demo.mp4 ./demo.mp4")
        elif ch == "17":
            os.system("adb shell dumpsys audio")
        elif ch == "18":
            os.system("adb shell dumpsys battery")
        elif ch == "19":
            os.system("adb shell getprop ro.product.model")
            os.system("adb shell getprop ro.build.version.release")
        elif ch == "20":
            os.system("adb shell am start -a android.settings.SETTINGS")
        elif ch == "21":
            break
        else:
            print("Invalid option.")
        input("Press Enter to continue...")

def main_menu():
    while True:
        print("""
CyberSecurityInvestigator Main Menu
1. PhoneSploit (ADB Toolkit)
2. SydSanusiCracker
3. Network Analysis
4. Vulnerability Scanner
5. Log Analysis
6. SQL Injection Detector
7. Exit
""")
        ch = input("Select option: ").strip()
        if ch == "1":
            phone_sploit_menu()
        elif ch == "2":
            sydsanusi_cracker()
        elif ch == "3":
            network_analysis()
        elif ch == "4":
            vulnerability_scanner()
        elif ch == "5":
            log_analysis()
        elif ch == "6":
            sql_injection_detector()
        elif ch == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
        input("Press Enter to continue...")

if __name__ == "__main__":
    verify_key()
    main_menu()
