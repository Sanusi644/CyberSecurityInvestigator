import os

def check_key():
    key = os.getenv("CSI_PRIVATE_KEY")
    if key != "SydSanusi@CyberKey#2025":
        print("❌ Invalid or missing private key.")
        print("📬 Contact: saminu644@gmail.com")
        exit(1)
    print("✅ Access granted. Welcome to Cyber Security Investigator.\n")

def main_menu():
    while True:
        print("""
==============================
📡 Cyber Security Investigator
==============================
1. Network Analysis
2. Vulnerability Scanner
3. Log Analysis
4. SQL Injection Detection
5. PhoneSploit (demo)
6. SydSanusiCracker (demo)
7. Exit
==============================
""")
        choice = input("👉 Select an option (1-7): ").strip()

        if choice == "1":
            print("[*] Simulating Network Scan...")
        elif choice == "2":
            print("[*] Simulating Vulnerability Scan...")
        elif choice == "3":
            print("[*] Simulating Log Analysis...")
        elif choice == "4":
            print("[*] Simulating SQLi Scan...")
        elif choice == "5":
            print("[*] Demo: PhoneSploit is not available in browser")
        elif choice == "6":
            print("[*] Demo: Crypto brute-force (simulation only)")
        elif choice == "7":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option.")
        input("\n🔁 Press Enter to return to menu...\n")

if __name__ == "__main__":
    check_key()
    main_menu()
