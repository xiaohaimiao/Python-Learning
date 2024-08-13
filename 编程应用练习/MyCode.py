import sys
import os

def print_color(text: str, color):
    colors = {
        "reset": "\033[0m",
        "red": "\033[031m",
        "green": "\033[032m",
        "yellow": "\033[033m",
        "blue": "\033[034m",
        "purple": "\033[035m",
        "cyan": "\033[036m",
        "white": "\033[037m",
        "gray": "\033[1;30m",
        "bright_red": "\033[1;31m",
        "bright_green": "\033[1;32m",
        "bright_yellow": "\033[1;33m",
        "bright_blue": "\033[1;34m",
        "bright_purple": "\033[1;35m",
        "bright_cyan": "\033[1;36m",
        "bright_white": "\033[1;37m"
    }
    print(f"{colors[color]}{text}{colors['reset']}")
    return

def print_error(text: str):
    print_color(text, "red")
    return

# 打开指定目录
def run_by_default_app(folder_path):
    if folder_path:
        if os.path.isdir(folder_path):
            os.system(f"explorer{folder_path}")
        else:
            os.startfile(folder_path)
    return