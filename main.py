import os

def check_key():
    key = os.getenv("CSI_PRIVATE_KEY")
    if key != "your-expected-key":
        print("❌ Invalid or missing private key.")
        print("📬 Please contact saminu644@gmail.com to request your private access key.")
        exit(1)

def main():
    check_key()
    print("✅ Tool started... More modules coming soon.")

if __name__ == "__main__":
    main()
