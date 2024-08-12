# 下载教材的小工具
# 作者：

# 版本：V1.0
# 主要功能：
# 从国家智慧教育平台下载教材
# 步骤：
# 1. 获取教材的 url
# 2. 获取教材的 HTML
# 3. 获取教材的下载地址
# 4. 下载教材到指定位置并命名
# 5. 输出结束信息

import os
import sys
import requests
# 添加上级目录到 sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MyCode import print_error, run_by_default_app, print_color

# 获取教材的 url
def get_book_url():
    if len(sys.argv) > 1:
        book_url = sys.argv[1]
    else:
        print_error("请提供有效的教材的 url")
    return book_url

# 获取教材的 HTML
def get_book_HTML(book_url):
    
    return

# 获取教材的下载地址
def get_book_pdf_url(book_HTML):
    
    return

# 下载教材到指定位置并命名
def book_down_load(book_pdf_url):
    
    return

def main():
    # 1. 获取教材的 url
    book_url = get_book_url()
    # 2. 获取教材的 HTML
    book_HTML = get_book_HTML(book_url)
    # 3. 获取教材的下载地址
    book_pdf_url = get_book_pdf_url(book_HTML)
    # 4. 下载教材到指定位置并命名
    book_pdf_file_path = book_down_load(book_pdf_url)
    # 5. 输出结束信息
    
    return

if __name__ == "__main__":
    main()