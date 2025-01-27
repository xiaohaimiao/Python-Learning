# 拆分试卷2
# 目标：
# 将 A3 试卷拆分成两张 A4 试卷
# 步骤：
# 1. 获取目标文件地址
# 2. 打开拆分目标图片文件
# 3. 以图片的中心线对半拆分图片
# 4. 将拆分后的图片分别保存到指定地点并重命名
# 5. 打开拆分后的图片的文件夹 
#
# V1.1：支持去弥封线、页眉、页角
# V1.2：支持六页卷

import sys
import os
from pdf2image import convert_from_path
from PIL import Image
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MyCode import print_error, run_by_default_app, print_color

def get_file_path():
    if len(sys.argv) <= 1:
        return None, "请提供目标文件的地址"

    file_path = sys.argv[1]
    # 判断地址是否有效
    if not os.path.isfile(file_path):
        return None, "请提供有效的文件。"
    # 判断是否是 PDF 文件
    if not file_path.endswith(".pdf"):
        return None, "请提供 PDF 格式文件的地址"
    return True, file_path

def split_pdf_file(source_file_path):
    # 3. 以图片宽的中心线对半拆分图片
    images = convert_from_path(source_file_path)
    
    # 3.2 枚举图像数组，拆分每一个图像到新的数组中
    
    # 3.3 将新的图像数组重新命名，并保存为新的PDF文件
    return True, output_file_path

def main():
    # 1. 获取目标文件地址
    result, message = get_file_path()
    if not result:
        print_error(message)
        return
    # 2. 打开拆分目标图片文件
    source_pdf_path = message
    output_pdf_path = split_pdf_file(source_pdf_path)
    # 5. 打开拆分后的图片的文件夹
    run_by_default_app(output_pdf_path)
    return True

if __name__ == "__main__":
    main()