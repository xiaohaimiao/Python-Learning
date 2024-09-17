# 基于 AI 的聊天工具
# 主要目标
# 接入 ChatGPT 的 API，实现交互式聊天
# 作者：loongba
# 版本：Ver 1.1

# 主要步骤：
# 1. 配置 ChatGPT API 的参数：access token
# 2. 调用第三方包，连接 API
# 3. 调用主函数，发送消息给 API
# 4. 接收 API 的返回值，显示给用户
# 5. 循环执行 3 和 4，直到用户退出

# Ver1.1
# 增加一个简单的用户交互界面：WebUI

import os
import sys
from openai import OpenAI
import streamlit as st

# 添加上级目录到 sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MyCode import print_error, run_file_by_default_app, print_color

def main():
    # 1. 配置 ChatGPT API 的参数：access token

    # 2. 调用第三方包，连接 API
    # 3. 调用主函数，发送消息给 API
    # 4. 接收 API 的返回值，显示给用户
    # 5. 循环执行 3 和 4，直到用户退出

    st.title("AI 聊天机器人")
    #st.markdown("与 AI 聊天，输入你的问题：")
    st.write("与 AI 聊天，请说：")

    user_input = st.text_input("你：", "")
    if user_input:
        ai_answer = chat_with_ai(user_input)
        st.write(ai_answer)

def chat_with_ai(question):
    client = OpenAI(api_key="sk-b4276afe3b344c29be0d95ea86d8085d", base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一位编程老师，需要给小朋友出一道编程方面的题目，并讲解。"},
            {"role": "user", "content": question},
        ],
        stream=False
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    main()
