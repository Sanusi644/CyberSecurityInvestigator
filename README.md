# 🔒 CyberSecurityInvestigator (CSI-Tool) v1.0

**Author:** Sanusi Saminu  
**GitHub:** [https://github.com/Sanusi644](https://github.com/Sanusi644)  
**Email:** saminu644@gmail.com  
**License:** MIT  

**Disclaimer:** This tool is for **legal and educational** cybersecurity research, digital forensics, ethical hacking, and Android device diagnostics only.

---

## 📌 Why I Created This Tool

Cybersecurity threats are growing rapidly, and many beginners and ethical hackers lack a simple, all-in-one tool for analysis, investigation, and learning. I built this tool to:

- Help educate ethical hackers and students  
- Provide an ADB-based Android investigation utility  
- Simulate brute-force for crypto wallets for educational demos  
- Analyze logs, scan for open ports, check for SQL vulnerabilities  
- Be lightweight and compatible with Termux and Linux  

---

## 🧰 Features & Modules

| Module Name              | Description                                                                      |
|--------------------------|----------------------------------------------------------------------------------|
| PhoneSploit (ADB)        | 25+ ADB commands to control Android devices via USB/Wi-Fi                       |
| SydSanusiCracker         | Simulates brute-force attacks on crypto wallets (educational only)             |
| Network Analysis         | Scans domains/IPs for open ports and services using nmap                        |
| Vulnerability Scanner    | Uses `curl` to check for HTTP headers, admin panels, and server leaks           |
| Log Analysis             | Analyzes system log files for failed login and brute-force attempts             |
| SQL Injection Detector   | Tests web URLs for common SQLi payloads (using `curl`)                          |

---

## 🖥️ Requirements

Before installation, make sure you have:

- Python 3.x (`pkg install python3`)  
- Termux or Linux  
- `git`, `nmap`, and `curl` installed  
- `adb` (Android Debug Bridge) installed and working  
- USB debugging enabled on your Android device  

---

## 🔧 Installation (Termux or Linux)

```bash
pkg update && pkg upgrade -y
pkg install python git nmap curl -y
pip install colorama

git clone https://github.com/Sanusi644/CyberSecurityInvestigator.git
cd CyberSecurityInvestigator

# Make sure adb is installed and accessible
pkg install android-tools  # On Termux
```

---

## ▶️ How to Run

Step 1: Run the tool with Python  
```bash
python3 csi.py
```

Step 2: Enter the investigator key when prompted  
📧 Contact `saminu644@gmail.com` for the private key

---

## 📡 Main Menu Overview

When you launch the tool, you’ll see:

```
CyberSecurityInvestigator - Main Menu  
1. PhoneSploit (ADB)  
2. SydSanusiCracker  
3. Network Analysis  
4. Vulnerability Scanner  
5. Log Analysis  
6. SQL Injection Detection  
7. Exit  
```

---

## 💻 How Each Module Works (Step-by-Step)

### 1. PhoneSploit (ADB)

Control Android devices via USB or Wi-Fi. Options include:

- Listing connected devices  
- Connecting via IP  
- Shell access  
- Reboot, lock screen, take screenshots  
- Push/pull files  
- Uninstall apps, get battery info, etc.

⚠️ **USB Debugging must be enabled on the Android phone.**

---

### 2. SydSanusiCracker

A simulated brute-force wallet cracker (educational only).

- Supports: Bitcoin, Ethereum, Tron, BNB, Litecoin  
- Requires a `.txt` dictionary wordlist  
- Simulates trying different mnemonics

❗ **Does not access real wallets.**

---

### 3. Network Analysis

- Scans any domain or IP for open ports and services  
- Uses `nmap -Pn <target>`

---

### 4. Vulnerability Scanner

- Checks for HTTP headers, open admin panels, etc.  
- Uses `curl -I <url>`

---

### 5. Log Analysis

- Analyzes system logs like `/var/log/auth.log`  
- Highlights failed SSH logins, brute-force signs

---

### 6. SQL Injection Detector

- Tests input URLs with common SQLi payloads  
- Uses `curl` to send crafted requests

---

## ⚠️ Legal Disclaimer

This tool is built strictly for ethical and educational use. You must have permission to run scans, access logs, or use ADB features on devices or networks.

❌ Never use it on systems you do not own  
❌ Do not use to harm, attack, or exploit others  
✅ For students, penetration testers, and digital forensics only

The author is not responsible for any misuse.

---

## 📬 Contact

If you need support, want to report bugs, or request collaboration:

- **Developer:** Sanusi Saminu  
- **Email:** saminu644@gmail.com  
- **GitHub:** [github.com/Sanusi644](https://github.com/Sanusi644)

---

## ⭐ Support This Project

If you find it useful:

- 🌟 Star the repository  
- 📤 Share with others in the cybersecurity community  
- 🛠️ Suggest improvements and report bugs via GitHub

---

## 📦 Coming Soon

- 📊 Live result logging  
- 🌐 Web panel integration  
- 📱 APK-based GUI wrapper  

Thank you for using CyberSecurityInvestigator. Be smart, ethical, and keep learning!
