# 接入 Chat GPT 的小程序
# 版本：V1.0
# 主要功能：
# 接入 Chat GPT
# 步骤：
# 1. 将用户的问题传给 Chat GPT 
# 2. 接收 Chat GPT 返回的值
# 3. 执行直到用户按Enter退出の
from openai import OpenAI
import os
import sys
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MyCode import print_error, run_file_by_default_app, print_color


def main():
    while True:
        question = input("请输入你的问题 （按 Enter 中止）")
        if len(question) == 0:
            break
        else:
            out_put = chat_wait_ai(question)
            print(f"{out_put}")
    return

def chat_wait_ai(question):
    
    return
if __name__ == "__main__":
    main()
