# 壁纸备份2
# 作用：
# 将桌面壁纸备份到指定文件夹中

# 步骤： 
# 1. 获取 windows聚焦 的地址
# 2. 获取指定文件夹地址（没有则创建）
# 3. 开始备份（并命名）
# 4. 返回结果
# V1.1 新增功能
# 1. 更改备份目录和备份文件名
#   1.1 改了备份的图片文件名
#   1.2 备份目录增加了子目录
# 2.可以备份锁屏背景
#V1.3 新增功能
# 为图片增加 Hash 值：Sha256

import sys
import os
import shutil
import datetime
import hashlib
import glob
import winreg
from PIL import Image as Image
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MyCode import print_error, run_by_default_app, print_color

# 获取锁屏壁纸地址
def get_windows11_lockscreen_folder():
    source_folder = os.path.expanduser(
        "~/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"
    )
    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_folder):
        # 获取文件的完整路径
        windows11_lockscreen_folder = os.path.join(source_folder, filename)
        
        # 检查目标是否为文件（而不是文件夹）
        if os.path.isfile(windows11_lockscreen_folder):
            return windows11_lockscreen_folder

# 获取桌面壁纸地址
def get_windows11_desktop_folder():
    # %userprofile%\AppData\Roaming\Microsoft\Windows\Themes\CachedFiles
    user_profile = os.getenv('USERPROFILE')
    path = f"{user_profile}\AppData\Roaming\Microsoft\Windows\Themes\CachedFiles"
    return path
# 获取“我的图片”地址
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

# 查找是否有相同的文件
def find_same_file(folder_path, filename):
    postfix = filename.split("_")[-2:] 
    searchPattern = f"*_{postfix[0]}_{postfix[1]}"   
    matchingFiles = glob.glob(os.path.join(folder_path, "**", searchPattern), recursive=True)
    return bool(matchingFiles)

# 复制壁纸
def copy_paper(file_folder1, file_folder2, prefix = "WallPaper"):
    if not os.path.isdir(file_folder1):
        print_error(f"源文件不存在: {file_folder1}")
        return False
    # 确保目标文件夹存在
    dst_dir = os.path.dirname(file_folder2)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
        
    year_month_str = datetime.datetime.now().strftime('%Y年%m月')
    sub_folder_path = os.path.join(file_folder2, year_month_str)
    
    for filename in os.listdir(file_folder1):
        src_file_path = os.path.join(file_folder1, filename)
        dst_new_filename = construct_image_filename(src_file_path, prefix)
        if not dst_new_filename:
            return
        dst_file_path = os.path.join(sub_folder_path, dst_new_filename)
        if (not find_same_file(file_folder2, dst_new_filename)):
            if not os.path.exists(sub_folder_path):
                os.makedirs(sub_folder_path)        
            shutil.copy2(src_file_path, dst_file_path)
    return

# 获取 hash 值
def get_file_hash(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'rb') as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

# 创造文件名
def construct_image_filename(image_path, prefix = "WallPaper"):
    file_size = os.path.getsize(image_path)
    file_size_str = f"{file_size // 1024},{file_size % 1024}"
    file_creation_time = os.path.getctime(image_path)
    file_create_time_str = datetime.datetime.fromtimestamp(file_creation_time).strftime('%Y%m%d')
    file_ext = "jpg"
    file_hash = get_file_hash(image_path)[:8]
    if not file_hash:
        print_error("无法获取有效的 hash 值！")
        return None
    img = Image.open(image_path)
    img_width, img_height = img.size
    img_resolution = f"{img_width}x{img_height}"
    new_file_name = f"{prefix}_{img_resolution}_{file_create_time_str}_{file_size_str}_{file_hash}.{file_ext}"
    return new_file_name

# 打开“我的图片”
def open_mypictures(file_folder):
    if file_folder:
        if os.path.isdir(file_folder):
            os.system(f"explorer {file_folder}")
        else:
            os.startfile(file_folder)
    return

def main():
    mypictures_folder = os.path.join(get_mypictures_folder(), "_备份壁纸_")
    windows11_lockscreen_folder = get_windows11_lockscreen_folder()
    copy_paper(windows11_lockscreen_folder, mypictures_folder, "WallPaper")
    # 备份桌面图片文件
    source_folder = get_windows11_desktop_folder()
    #open_folder(source_folder)
    # 复制桌面图片：命名规则有所变化
    copy_paper(source_folder, mypictures_folder, "Desktop")
    print_color(f"成功！", "green")
    # 打开“我的图片_壁纸备份_”
    open_mypictures(mypictures_folder) 
    return

if __name__ == "__main__":
    main()