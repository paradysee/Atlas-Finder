from commands.utils import *
from commands.phone import run as phone_run
from commands.ip import run as ip_run


def startup_menu():
    info("Atlas")
    print("""
          Welcome to Atlas Finder!

 (1) IP        → IP lookup
 (2) Phone     → Phone lookup

 Type 'Help' to see all commands.
""")


def help_menu():
    info("Available Commands...")
    print("""
 IP <address>        Example: IP 8.8.8.8
 Phone <number>      Example: Phone +521234567890

 Clear               Clear screen
 Help                Show this menu
 Exit                Close Atlas
""")


def main():
    clear()
    banner()
    startup_menu()

    while True:
        cmd = input("\natlas@user:-$ ").strip()

        if not cmd:
            continue

        cmd_lower = cmd.lower()

        if cmd_lower.startswith("ip "):
            ip = cmd.split(" ", 1)[1]
            result = ip_run(ip)

            if not result:
                warn("Usage: ip (adress)")
            else:
                for k, v in result.items():
                    success(f"{k}: {v}")

        elif cmd_lower.startswith("phone "):
            phone = cmd.split(" ", 1)[1]
            result = phone_run(phone)

            if not result:
                warn("Usage: phone (number)")
            else:
                for k, v in result.items():
                    success(f"{k}: {v}")

        elif cmd_lower == "clear":
            clear()
            banner()
            startup_menu()

        elif cmd_lower == "help":
            help_menu()

        elif cmd_lower == "exit":
            info("Closing Atlas...")
            break

        else:
            warn("Unknown command. Type 'Help' for available commands.")


if __name__ == "__main__":
    main()

