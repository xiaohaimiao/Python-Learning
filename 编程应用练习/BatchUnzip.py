import os
import zipfile
import PyPDF2

def batch_unzip(directory):
    """
    批量解压缩指定目录下的 zip 文件到 zip 子目录下

    参数:
    directory (str): 指定目录的路径

    返回:
    无
    """
    # 创建 zip 子目录
    zip_dir = os.path.join(directory, 'zip')
    os.makedirs(zip_dir, exist_ok=True)

    # 遍历指定目录下的文件
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        # 判断文件是否为 zip 文件
        if file.endswith('.zip') and os.path.isfile(file_path):
            print(f'Unzipping {file_path} to {zip_dir}')
            # 解压缩 zip 文件到 zip 子目录下
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(zip_dir)
    return zip_dir

# 将多个 pdf 文件合并为一个 pdf 文件，并更改名字
def merge_pdf_files(directory, filename=""):
    """
    将多个 pdf 文件合并为一个 pdf 文件，并更改名字

    参数:
    directory (str): 指定目录的路径
    filename (str): 合并后的文件名，默认为空字符串

    返回:
    无
    """
    # 创建一个空的 PDFWriter 对象
    pdf_writer = PyPDF2.PdfFileWriter()

    # 遍历指定目录下的文件
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        # 判断文件是否为 pdf 文件
        if file.endswith('.pdf') and os.path.isfile(file_path):
            print(f'Merging {file_path} into {filename}')
            # 打开 pdf 文件并将其添加到 PDFWriter 对象中
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                for page_num in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(page_num)
                    pdf_writer.addPage(page)

    # 保存合并后的 pdf 文件
    output_path = os.path.join(directory, filename)
    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

    print(f'Merged PDF saved as {output_path}')
if __name__ == "__main__":
    # 调用函数并传入指定目录的路径
    #path = '/path/to/directory'
    path = 'X:\__学习资源__\_电子书_\[书籍、资料]\[IT技术]\计算机科学\数据结构算法与应用-C++语言描述'
    #zip_dir = batch_unzip(path)
    zip_dir = path + "\zip"
    merge_pdf_files(zip_dir, "数据结构算法与应用-C++语言描述.pdf")
    