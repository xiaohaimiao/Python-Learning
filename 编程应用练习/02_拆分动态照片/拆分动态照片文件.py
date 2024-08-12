# 拆分动态照片文件工具
# 主要功能：
# 将指定的动态照片文件拆分为个一个照片文件与一个视频文件

# 作者：xiaohai
# 日期：2024/07/26
# 版本：v1.0

# 分解步骤：
# 1. 获取目标文件的路径
# 2. 创建两个接收文件夹（分别命名“照片”与“视频”）
# 3. 找到并复制文件中的照片与视频（分别复制到两个对应文件夹）
#
# V1.1  2024/07/29  对文件夹中的所有动态照片进行拆分
# V1.2  2024/07/29  加入颜色控制符
# TODO:
# V1.3  2024/07/29  加入命令行参数，用于指定要拆分动态照片的文件夹

import os
import sys

def main():    
    # 1. 获取目标文件的路径
    if len(sys.argv) <= 1:
        #   获取当前脚本所在目录
        folder = os.path.dirname(os.path.abspath(__file__))
    else:
        argument = sys.argv[1]
        if os.path.isdir(argument):
            folder = argument
        else:
            print(f"\033[31m参数不是有效文件夹：{argument}\033[0m")
            return 
    # 2.  查找该目录下所有 jpg 文件并处理
    output_folder = do_with_files_in_folder(folder, "_Output_")
    
    # 4. 用资源管理器打开输出文件夹
    open_folder(output_folder)
    return


def do_with_file(photo_file_path, sub_folder_name="_Output_", keyword="MotionPhoto_Data"):
    # 读取指定的文件
    with open(photo_file_path, "rb") as file_jpg:
        file_content = file_jpg.read()
        
    photo_filename = os.path.basename(photo_file_path)    # 取文件名
    # 查找关键字
    index = file_content.find(keyword.encode())
    if index == -1:
        # 找不到，退出：返回失败信息
        return None, f"{photo_filename} 不是动态照片", None
    output_folder = os.path.join(os.path.dirname(photo_file_path), sub_folder_name)
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    # 输出文件需要放到输出文件夹
    # 构造两个文件名，分别为照片文件名、视频文件名 ".jpg" "_Photo.jpg"  "_Video.mp4"
    jpg_filename = photo_filename.lower().replace(".jpg", "_Photo.jpg")
    mp4_filename = photo_filename.lower().replace(".jpg", "_Video.mp4")

    # 则将关键字位置前、后内容分别保存为两个文件
    with open(os.path.join(output_folder, jpg_filename), "wb") as f:
        f.write(file_content[:index])
        
    with open(os.path.join(output_folder, mp4_filename), "wb") as f:
        f.write(file_content[index + len(keyword):])
    # 返回操作成功信息
    return output_folder, jpg_filename, mp4_filename

def do_with_files_in_folder(folder, sub_folder_name="_Output_", keyword="MotionPhoto_Data"):
    # 用循环遍历指定路径下的所有文件
    # 遍历，并复制文件到目标文件夹
    print(f"拆分 {folder} 文件夹中的动态照片：")
    count = 0
    for filename in os.listdir(folder):
        if os.path.isdir(filename):
            continue
        file_extension = filename.split(".")[-1].lower()
        if file_extension in ["jpg", "jpeg", "png"]:
        #if filename.lower().endswith(".jpg"):
            file_path = os.path.join(folder, filename)
            subfolder, jpg_filename, mp4_filename  = do_with_file(file_path, sub_folder_name, keyword)
            if subfolder == None:
                print(f"\t\033[31m拆分失败：{jpg_filename}\r\n\t\t{file_path}\033[0m")
            else:
                # 3. 输出结束信息
                count += 1
                output_folder = subfolder
                print(f"\t\033[32m{count:2d} 拆分成功：{filename}\r\n\t\t{jpg_filename}\r\n\t\t{mp4_filename}\033[0m")
    return output_folder


def open_folder(folder_path):
    if folder_path:
        if os.path.isdir(folder_path):
            os.system("explorer " + folder_path)
        else:
            os.startfile(folder_path)
    return

if __name__ == "__main__":
    main()
