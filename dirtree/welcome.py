import os
import re
from colorama import Fore, Style, init

init(autoreset=True)

def strip_ansi(line):
    # Retire toutes les séquences ANSI
    return re.sub(r'\x1b\[[0-9;]*m', '', line)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def welcome():
    clear_screen()
    lines = [
        f"{Fore.GREEN}Welcome to the Dirtree tool!{Style.RESET_ALL}",
        f"{Fore.LIGHTGREEN_EX}Macxzew{Style.RESET_ALL} | {Fore.MAGENTA}v1.0{Style.RESET_ALL}",
        f"{Fore.WHITE}{'-' * 40}{Style.RESET_ALL}",
        "",
        f"{Fore.YELLOW}This tool lets you:{Style.RESET_ALL}",
        "  - Display your folder structure.",
        "  - Export it as a formatted .txt file.",
        "  - Use a GUI for folder and save location selection.",
        "",
    ]

    # Largeur ajustée à la plus longue ligne sans couleur + 2 espaces de chaque côté (bordures)
    content_width = max(len(strip_ansi(line)) for line in lines)
    total_width = content_width + 2  # 1 espace à gauche + 1 à droite

    # Top border
    print(f"{Fore.CYAN}{Style.BRIGHT}╔{'═' * total_width}╗{Style.RESET_ALL}")

    for i, line in enumerate(lines):
        visible = strip_ansi(line)
        padding = total_width - len(visible)
        if not visible:
            # Ligne vide : juste espaces entre les bords
            print(f"║{' ' * total_width}║")
        elif i < 4:
            # Les 4 premières lignes centrées dans le cadre
            left = padding // 2
            right = padding - left
            print(f"║{' ' * left}{line}{' ' * right}║")
        else:
            # Autres lignes alignées à gauche avec 1 espace à droite (pro)
            print(f"║ {line}{' ' * (total_width - len(visible) - 1)}║")
    # Bottom border
    print(f"{Fore.CYAN}{Style.BRIGHT}╚{'═' * total_width}╝{Style.RESET_ALL}")

if __name__ == "__main__":
    welcome()
