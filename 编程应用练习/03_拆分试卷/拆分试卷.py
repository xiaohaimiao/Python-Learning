# 作者：
# 版本号： 1.0
# 作用：
# 将一个A3试卷对半拆分， 并打包为一个新文件

# 分解步骤：
# 1. 获取指定PDF文件
# 2. 导出PDF文件
# 3. 拆分文件并为其命名
# 4. 保存拆分后的文件到一个目录内
# 5. 输出结束信息
import os
import sys
from pdf2image import convert_from_path
# 添加上级目录到 sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MyCode import print_error, run_by_default_app, print_color

def main():
    # 1. 获取目标文件的路径
    pdf_file_path, new_pdf_file_path = get_pdf_file_path()
    if not pdf_file_path:
        return
    # 2. 导出PDF文件
    image_list = split_pdf_into_images(pdf_file_path)
    if image_list:
        # 4. 包装图片
        result, message = merged_image_into_PDF(image_list, new_pdf_file_path)
        if result:
            # 5. 输出结束信息
            print_color(f"拆分PDF文件成功： {new_pdf_file_path}", "green")
            run_by_default_app(new_pdf_file_path)
            run_by_default_app(os.path.dirname(new_pdf_file_path))
        else:
            print_error(f"合并PDF文件失败： {message}")
    else:
        print_error(f"拆分PDF文件失败： {new_pdf_file_path}")

    return

def split_pdf_into_images(pdf_file_path):
    if not os.path.exists(pdf_file_path):
        print_color(f"文件不存在：{pdf_file_path}")
        return None

    # 判断文件是否是PDF
    pdf_filename = os.path.basename(pdf_file_path)    # 取文件名
    if not pdf_filename.endswith(".pdf"):
        return None

    # 调用第三方包，将 PDF 文件每一页拆分为一个图片文件，并保存到指定目录
    # 将PDF转换为图片
    pages_images = convert_from_path(pdf_file_path)
    image_list = []
    # 将图片保存到指定目录
    for i, page_image in enumerate(pages_images):
        page_number = i + 1
        # 3. 拆分文件并为其命名
        images = split_image_into_images(page_image)
        image_list.extend(images)
    return image_list

# 将图片以宽度的一半拆分为两部分
def split_image_into_images(page_image):
    # 获取图片的宽度和高度
    width, height = page_image.size

    # 计算新的宽度
    new_width = width // 2

    # 创建两个新的图像
    image1 = page_image.crop((0, 0, new_width, height))
    image2 = page_image.crop((new_width, 0, width, height))
    # 返回两个新的图像
    return [image1, image2]

def merged_image_into_PDF(image_list, pdf_file_path):
    if not image_list:
        return False, "image_list 图像列表为空"
    try:    # 尝试
        image_list[0].save(pdf_file_path, save_all = True, append_images = image_list[1:])
        return True, pdf_file_path
    except Exception as e:  # 例外
        return False, str(e)

def get_pdf_file_path():
    if len(sys.argv) > 1:
        pdf_file_path = sys.argv[1]
        if not os.path.isabs(pdf_file_path):
            # 尝试相对于当前工作目录
            current_folder = os.curdir()
            pdf_file_path = os.path.join(current_folder, pdf_file_path)
            if not is_pdf(pdf_file_path):    
                # 尝试相对于脚本所在目录
                script_folder = os.path.dirname(os.path.abspath(__file__))
                pdf_file_path = os.path.join(script_folder, pdf_file_path)

        if is_pdf(pdf_file_path):
            new_pdf_file_path = pdf_file_path.replace(".pdf", "_A4.pdf")
            return pdf_file_path, new_pdf_file_path
        else:
            print_error(f"参数不是有效的 PDF 文件：{pdf_file_path}")
    else:
        print_error(f"请提供 PDF 文件的完整路径。")
    return None, None

def is_pdf(pdf_file_path):
    return os.path.isfile(pdf_file_path) and pdf_file_path.lower().endswith(".pdf")



if __name__ == "__main__":
    main()