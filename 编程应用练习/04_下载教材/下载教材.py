# 下载教材的小工具
# 作者：

# 版本：V1.0
# 主要功能：
# 从国家智慧教育平台下载教材
# 步骤：
# 1. 获取教材的 url
# 2. 获取教材的下载地址的 url
# 3. 下载教材到指定位置并命名
# 4. 输出结束信息


import os
import requests
import sys
import re

# 添加上级目录到 sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MyCode import print_error, run_by_default_app, print_color

# 获取教材的 url
def get_args():
    #book_guid_or_url = "https://basic.smartedu.cn/tchMaterial/detail?contentType=assets_document&contentId=8b9c7052-add4-4744-ab04-69d6c180d5d9&catalogType=tchMaterial&subCatalog=tchMaterial"
    #book_guid_or_url = "8b9c7052-add4-4744-ab04-69d6c180d5d9"
    #book_name = "义务教育教科书·语文七年级上册"
    if len(sys.argv) > 2:
        book_guid_or_url = sys.argv[1]
        book_name = sys.argv[2]
    else:
        print_error("请提供有效的教材的 url 和名字")
    return book_guid_or_url, book_name

# 获取教材的下载地址的 url
def get_book_pdf_url(url_or_guid):
    #url_or_guid = "https://basic.smartedu.cn/tchMaterial/detail?contentType=assets_document&contentId=8b9c7052-add4-4744-ab04-69d6c180d5d9&catalogType=tchMaterial&subCatalog=tchMaterial"
    #url_or_guid = "8b9c7052-add4-4744-ab04-69d6c180d5d9"
    
    pattern = r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
    match = re.search(pattern, url_or_guid)

    if match:
        book_guid = url_or_guid
    else:
        pattern = r'contentId=(.*?)(&|$)'
        match = re.search(pattern, url_or_guid)
        if match:
            book_guid = match.group(1)
        else:
            #print_error(f"url_or_guid 没有包含教材的 GUID：{url_or_guid}")
            return None
    book_pdf_url = f"https://r1-ndr.ykt.cbern.com.cn/edu_product/esp/assets_document/{book_guid}.pkg/pdf.pdf"
    #book_pdf_url = f"{book_guid}"
    return book_pdf_url


# 下载教材到指定位置并命名
def download_file(file_url, full_filename):
    try:
        r = requests.get(file_url)
        with open(full_filename, 'wb') as f:
            f.write(r.content)
    except Exception as e:
        return False, e

    return True, full_filename
    
def main():
    # 获取教材的 url 和名字
    book_url_or_guid, book_name = get_args()
    
    # 获取教材的下载地址
    book_pdf_url = get_book_pdf_url(book_url_or_guid)
    if not book_pdf_url:
        print_error(f"请输入有效的 url/GUID 和名字 {book_url_or_guid} {book_name}")
        return
    
    # 下载教材到指定位置并命名
    output_folder = "_教材_"
    os.makedirs(output_folder)
    book_pdf_file_path = f"{output_folder}\\{book_name}.pdf"
    success, book_pdf_file_path = download_file(book_pdf_url, book_pdf_file_path)
    
    # 输出结束信息
    if not success:
        print_error(f"错误：{book_pdf_file_path}")
        return
    else:
        print_color(f"成功！{book_pdf_file_path}", "green")
        # 打开
        run_by_default_app(book_pdf_file_path)
    return

if __name__ == "__main__":
    main()