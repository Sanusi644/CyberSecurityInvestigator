#!/data/data/com.termux/files/usr/bin/bash

echo "Installing dependencies..."
pkg update -y && pkg upgrade -y
pkg install git python3 adb -y
pip install colorama

echo "Installation complete. You can now run the tool with: python3 cyber_investigator.py"
