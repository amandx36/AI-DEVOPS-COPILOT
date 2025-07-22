import colorama
from colorama import Fore, Back, Style

colorama.init()

def show_banner():
    # Define the ASCII art lines with color assignments for a gradient effect
    banner_lines = [
        (r"_   _  _____                _____                _    _        ___        ", Fore.LIGHTCYAN_EX + Style.BRIGHT),
        (r"| \ | ||____ |              /  ___|              | |  | |      /   |       ", Fore.CYAN + Style.BRIGHT),
        (r"|  \| |    / /__  __ ______ \ `--.  _   _  _ __  | |_ | |__   / /| | _ __  ", Fore.LIGHTMAGENTA_EX + Style.BRIGHT),
        (r"| . ` |    \ \\ \/ /|______| `--. \| | | || '_ \ | __|| '_ \ / /_| || '__| ", Fore.MAGENTA + Style.BRIGHT),
        (r"| |\  |.___/ / >  <         /\__/ /| |_| || | | || |_ | | | |\___  || |    ", Fore.LIGHTBLUE_EX + Style.BRIGHT),
        (r"\| \_/\____/ /_/\_\        \____/  \__, ||_| |_| \__||_| |_|    |_/|_|    ", Fore.BLUE + Style.BRIGHT),
        (r"                                    __/ |                                 ", Fore.LIGHTBLUE_EX + Style.BRIGHT),
        (r"                                   |___/                                  ", Fore.BLUE + Style.BRIGHT),
        (r"", Fore.RESET),  # Empty line
        (r"      AI DEVOPS COPILOT CLI TOOL", Fore.LIGHTYELLOW_EX + Back.BLACK + Style.BRIGHT),
        (r"    --------------------------------", Fore.YELLOW + Style.BRIGHT),
    ]

    # Print the main banner
    for line, color in banner_lines:
        print(color + line + Style.RESET_ALL)

    # Holographic effect for the signature with vibrant, fast-changing colors
    credit = "  N3xthar-Voryx (Aman Deep)"
    colors = [
        Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, 
        Fore.LIGHTMAGENTA_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX
    ]  # Vibrant, fast-changing gradient
    colored_credit = ""
    for i, char in enumerate(credit):
        colored_credit += colors[i % len(colors)] + Style.BRIGHT + char
    print(colored_credit + Style.RESET_ALL)

if __name__ == "__main__":
    show_banner()