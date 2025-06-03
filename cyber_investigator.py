import os
from colorama import Fore

def banner():
    print(Fore.CYAN + '''
  ____       _     _                 _       _             _       
 / ___|  ___| |__ (_) ___  _ __   __| | __ _| |_   _  __ _| |_ ___ 
 \___ \ / __| '_ \| |/ _ \| '_ \ / _` |/ _` | | | | |/ _` | __/ _ \
  ___) | (__| | | | | (_) | | | | (_| | (_| | | |_| | (_| | ||  __/
 |____/ \___|_| |_|_|\___/|_| |_|\__,_|\__,_|_|\__,_|\__,_|\__\___|

    ''' + Fore.RESET)

def main():
    os.system("clear")
    banner()
    key = input("Enter your license key: ").strip()
    if key == "SYDSANUSI-2025-KEY123":
        print(Fore.GREEN + "License verified! Starting the tool..." + Fore.RESET)
        # Future features or modules can go here
    else:
        print(Fore.RED + "Invalid license key. Exiting..." + Fore.RESET)

if __name__ == "__main__":
    main()
