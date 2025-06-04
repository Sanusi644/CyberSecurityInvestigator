import os

def check_key():
    key = os.getenv("CSI_PRIVATE_KEY")
    if key != "SydSanusi@CyberKey#2025":
        print("❌ Invalid or missing private key.")
        print("📬 Please contact saminu644@gmail.com to request your private access key.")
        exit(1)
    print("✅ Access granted. Welcome to Cyber Security Investigator.")

check_key()

# Your existing main.py code continues here...
