# 壁纸备份2
# 作用：
# 将桌面壁纸备份到指定文件夹中

# 步骤： 
# 1. 获取 windows聚焦 的地址
# 2. 获取指定文件夹地址（没有则创建）
# 3. 开始备份（并命名）
# 4. 返回结果
# V1.1 新增功能：更改备份目录和备份文件名
#   A. 改了备份的图片文件名
#   B. 备份目录增加了子目录
# V1.2 新增功能：可以备份锁屏背景
# V1.3 新增功能：为图片增加 Hash 值：Sha256
# V1.4 新增功能：记录日志
# V1.5 新增功能：优化避免重复计算文件 Hash 值（在来源目录记录文件hash值）

import sys
import os
import shutil
import datetime
import hashlib
import glob
import winreg
import logging
import json as Json
from PIL import Image as Image
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MyCode import print_error, run_by_default_app, print_color

# 获取锁屏壁纸地址
def get_windows11_lockscreen_folder():
    source_folder = os.path.expanduser(
        f"~\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
    )
    return source_folder

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
def find_same_file_by_hash(folder_path, filename):
    postfix = filename.split("_")[-2:]
    searchPattern = f"*_{postfix[0]}_{postfix[1]}"
    matchingFiles = glob.glob(os.path.join(folder_path, "**", searchPattern), recursive=True)
    return bool(matchingFiles)

# 查找目标文件数据是否存在
def find_log(logs, filename):
    for log in logs:
        if filename == log["SourceFile"]:
            return log
    return None

# 判断指定文件的记录是否存在于数据文件中
def if_backup_log_exists(filename):
    # 判断数据文件是否存在
    log_file_path = os.path.join(backup_pictures_folder, "备份记录.json")
    if not os.path.exists(log_file_path):
        return False
    # 读取数据文件的内容
    with open(log_file_path, "r", encoding = "utf-8") as file:
        logs = Json.load(file)
    # 判断目标文件是否存在于数据中
    log = find_log(logs, filename)
    return log != None

# 保存备份记录
def write_backup_log(filename, dst_new_filename):
    # 判断文件是否存在
    if os.path.exists(log_file_path):
        # 读取数据文件的内容
        with open(log_file_path, "r", encoding = "utf-8") as file:
            logs = Json.load(file)
        if not logs:
            logs = []
    else:
        # 新建数据记录对象
        logs = []

    # 判断目标文件是否存在于数据中
    log = find_log(logs, filename)
    if log:
        log["BackupFile"] = dst_new_filename
    else: 
        logs.append({"SourceFile":filename, "BackupFile":dst_new_filename})
    # 写入数据文件
    with open(log_file_path, "w", encoding = "utf-8") as file:
        Json.dump(logs, file)

    return log_file_path

# 复制壁纸
def copy_pictures(source_folder, destination_folder, prefix = "WallPaper"):
    if not os.path.isdir(source_folder):
        print_error(f"源文件不存在: {source_folder}")
        return False
    # 确保目标文件夹存在
    os.makedirs(destination_folder, exist_ok=True)
        
    year_month_str = datetime.datetime.now().strftime('%Y年%m月')
    sub_folder_path = os.path.join(destination_folder, year_month_str)
    os.makedirs(sub_folder_path, exist_ok=True)
    
    # 遍历/枚举 来源文件夹中的所有文件
    for filename in os.listdir(source_folder):
        if if_backup_log_exists(filename):    # 判断 Hash 记录是否存在
            print_color(f"{filename}文件已存在记录", "yellow")
            continue 
        src_file_path = os.path.join(source_folder, filename)
        dst_new_filename = create_image_filename(src_file_path, prefix)
        if dst_new_filename == None:
            print_error(f"create_image_filename({src_file_path}, {prefix}) 失败，忽略当前文件。")
            continue
        dst_file_path = os.path.join(sub_folder_path, dst_new_filename)
        if (not find_same_file_by_hash(destination_folder, dst_new_filename)):
        #if (find_same_file(file_folder2, dst_new_filename)):
            shutil.copy2(src_file_path, dst_file_path)
            # 保存备份记录
            write_backup_log(filename, dst_new_filename)
    return

# 获取 hash 值
def compute_file_hash(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'rb') as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

# 创造文件名
def create_image_filename(image_path, prefix = "WallPaper"):
    file_size = os.path.getsize(image_path)
    file_size_str = f"{file_size // 1024},{file_size % 1024}"
    file_creation_time = os.path.getctime(image_path)
    file_create_time_str = datetime.datetime.fromtimestamp(file_creation_time).strftime('%Y%m%d')
    file_ext = "jpg"
    file_hash = compute_file_hash(image_path)[:8]
    if not file_hash:
        print_error("无法获取有效的 hash 值！")
        return None
    img = Image.open(image_path)
    img_width, img_height = img.size
    img_resolution = f"{img_width}x{img_height}"
    new_file_name = f"{prefix}_{img_resolution}_{file_create_time_str}_{file_size_str}_{file_hash}.{file_ext}"
    return new_file_name

def main():
    lockscreen_wallpaper_folder = get_windows11_lockscreen_folder()
    copy_pictures(lockscreen_wallpaper_folder, backup_pictures_folder, "WallPaper")
    print_color(f"WallPaper 成功！", "green")
    # 备份桌面图片文件
    desktop_wallpaper_folder = get_windows11_desktop_folder()
    #open_folder(source_folder)
    # 复制桌面图片：命名规则有所变化
    copy_pictures(desktop_wallpaper_folder, backup_pictures_folder, "Desktop")
    print_color(f"Desktop 成功！", "green")
    # 打开“我的图片_壁纸备份_”
    run_by_default_app(backup_pictures_folder)
    return

if __name__ == "__main__":
    backup_pictures_folder = os.path.join(get_mypictures_folder(), "_备份壁纸_")
    log_file_path = os.path.join(backup_pictures_folder, "备份记录.json")
    # 记录日志
    logging.basicConfig(level=logging.INFO,
    filename = os.path.join(backup_pictures_folder,"日志.log"),  # 日志写入文件
    format = '%(asctime)s - %(message)s')
    filemode = 'a',        # 写入模式，'w' 覆盖写入，'a' 追加写入
    logging.info("开始运行")
    try:
        main()
    except ZeroDivisionError as e:
        logging.error('发生了一个错误：', exc_info=True)
    logging.info('程序结束')