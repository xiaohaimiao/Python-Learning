import sys
import os


def print_color(text: str, color="green"):
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

# 用默认程序运行指定的文件


def run_by_default_app(file_path):
    # 确保是绝对路径
    file_path = os.path.abspath(file_path) 
        
    #os.startfile(file_path)
    if os.path.isdir(file_path):
        if os.name == "NT":
            # path 环境变量里
            os.system(f"explorer.exe {file_path}")
    else:
        os.startfile(file_path)

    return

# 打开指定目录
def open_folder(folder_path):
    if not os.path.isabs(folder_path):
        folder_path = os.path.abspath(folder_path)

    if not os.path.isdir(folder_path):
        folder_path = os.path.dirname(folder_path)

    os.system(f"explorer {folder_path}")
    return