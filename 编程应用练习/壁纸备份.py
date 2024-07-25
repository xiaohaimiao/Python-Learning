# 主要功能：
# 1. 备份桌面壁纸：Windows 11 的 "Windows 聚焦" 的图片
# 2. 默认被分到文件夹：“我的图片/_壁纸备份_”，可以指定备份文件夹

# 作者：xiaohai
# 日期：2024/07/23
# 版本：1.0

# 分解：
# 1. 找到Windows 11 的 "Windows 聚焦" 的图片的地址
# 2. 找到指定文件夹的地址
# 3. 将图片备份到指定文件夹并提示“已备份”
# 4. 用文件资源管理器打开备份文件夹

# V1.1 新增功能
# 1. 更改备份目录和备份文件名
#   1.1 备份的图片文件名改为：WallPaper_1920x1080_20240724_572,201.jpg（572,201 是文件的存储大小）
#   1.2 备份目录增加了 2024年07月 的子目录
#V1.2 新增功能
# 1. 备份桌面背景图片：%userprofile%\AppData\Roaming\Microsoft\Windows\Themes\CachedFiles

#V1.3 为图片增加 Hash 值：MD5/Sha256
#   用 Hash 值来判断是否有重复图片

import os
import winreg
import shutil
from PIL import Image as Image
import datetime as dt

# 取出Windows聚焦的图片的地址
def get_windows11_lockscreen_folder():
    user_profile = os.getenv('USERPROFILE')
    content_delivery_manager_path = os.path.join(
        user_profile, 'AppData', 'Local', 'Packages')

    # 查找 Microsoft.Windows.ContentDeliveryManager 的子文件夹
    for root, dirs, files in os.walk(content_delivery_manager_path):
        for dir_name in dirs:
            if 'Microsoft.Windows.ContentDeliveryManager' in dir_name:
                return os.path.join(root, dir_name, 'LocalState', 'Assets')

    return None

#
def get_windows11_desktop_folder():
    # %userprofile%\AppData\Roaming\Microsoft\Windows\Themes\CachedFiles
    user_profile = os.getenv('USERPROFILE')
    path = f"{user_profile}\AppData\Roaming\Microsoft\Windows\Themes\CachedFiles"
    return path

# 取出“我的图片_壁纸备份_”的地址
def get_mypictures_folder():
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders",
    )
    folders = dict(
        [(winreg.EnumValue(key, i)[:2])
        for i in range(winreg.QueryInfoKey(key)[1])]
    )
    return folders.get("My Pictures")

# 将Windows聚焦的所有图片复制到“我的图片_壁纸备份_”
def copy_files(src_folder_path, dst_folder_path, prefix = "WallPaper"):
    # 确保源文件夹存在
    if not os.path.isdir(src_folder_path):
        print(f"源文件不存在: {src_folder_path}")
        return False

    # 确保目标文件夹存在
    dst_dir = os.path.dirname(dst_folder_path)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    
    # 获取今日年月，如：2024年8月
    year_month_str = dt.datetime.now().strftime('%Y年%m月')
    dst_folder_path = os.path.join(dst_folder_path, year_month_str)
    # 确保年月子目录存在
    if not os.path.exists(dst_folder_path):
        os.makedirs(dst_folder_path)
    # 遍历，并复制文件到目标文件夹
    for filename in os.listdir(src_folder_path):
        src_file_path = os.path.join(src_folder_path, filename)
        dst_new_filename = construct_image_filename(src_file_path, prefix)
        dst_file_path = os.path.join(dst_folder_path, dst_new_filename)
        print("src_file_path", src_file_path)
        print("dst_file_path", dst_file_path)
        shutil.copy2(src_file_path, dst_file_path)

    return True

# 函数：构造图片文件的名字，并返回
# 基于指定图片文件的信息构造，规则为 WallPaper_1920x1080_20240724_572,201.jpg
# 其中，“1920x1080”是图片分辨率，“20240724”是图片创建日期，“572,201” 是文件的存储大小
def construct_image_filename(image_path, prefix = "WallPaper"):
    # 获取文件大小
    file_size = os.path.getsize(image_path)
    file_size_str = f"{file_size // 1024},{file_size % 1024}"

    # 获取文件的创建日期，构造新文件名中的日期部分
    file_creation_time = os.path.getctime(image_path)  # 获取文件创建时间
    file_create_time_str = dt.datetime.fromtimestamp(file_creation_time).strftime('%Y%m%d')  # 将时间戳转换为日期格式
    file_ext = ".jpg"
    
    # 获取图片的长、宽，用于构造文件名中的分辨率部分
    img = Image.open(image_path)
    img_width, img_height = img.size
    img_resolution = f"{img_width}x{img_height}"

    # 构造新的文件名
    new_file_name = f"{prefix}_{img_resolution}_{file_create_time_str}_{file_size_str}{file_ext}"

    # 返回新的文件名
    return new_file_name

# 打开“我的图片_壁纸备份_”
def open_folder(folder_path):
    if os.path.isdir(folder_path):
        os.startfile(folder_path)
    else:
        print(f"指定的路径不是一个有效的文件夹: {folder_path}")


def main():
    dest_folder = os.path.join(get_mypictures_folder(), "_备份壁纸_")

    source_folder = get_windows11_lockscreen_folder()
    copy_files(source_folder, dest_folder, "WallPaper")
    
    # 备份桌面图片文件
    source_folder = get_windows11_desktop_folder()
    #open_folder(source_folder)
    # 复制桌面图片：命名规则有所变化
    copy_files(source_folder, dest_folder, "Desktop")
    open_folder(dest_folder)
    return

if __name__ == "__main__":
    main()
