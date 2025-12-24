import os
from colorama import Fore, init

init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(Fore.LIGHTBLUE_EX + r"""
 █████╗ ████████╗██╗      █████╗ ███████╗
██╔══██╗╚══██╔══╝██║     ██╔══██╗██╔════╝
███████║   ██║   ██║     ███████║███████╗
██╔══██║   ██║   ██║     ██╔══██║╚════██║
██║  ██║   ██║   ███████╗██║  ██║███████║
╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝
         v1.0.1
""")

def success(msg):
    print(Fore.GREEN + "[+] " + str(msg))

def info(msg):
    print(Fore.CYAN + "[*] " + str(msg))

def warn(msg):
    print(Fore.YELLOW + "[!] " + str(msg))

def error(msg):
    print(Fore.RED + "[-] " + str(msg))
