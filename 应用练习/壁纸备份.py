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
import os
import winreg
import shutil

# 取出Windows聚焦的图片的地址
def get_windows11_spotlight_folder():
    user_profile = os.getenv('USERPROFILE')
    content_delivery_manager_path = os.path.join(
        user_profile, 'AppData', 'Local', 'Packages')

    # 查找 Microsoft.Windows.ContentDeliveryManager 的子文件夹
    for root, dirs, files in os.walk(content_delivery_manager_path):
        for dir_name in dirs:
            if 'Microsoft.Windows.ContentDeliveryManager' in dir_name:
                return os.path.join(root, dir_name, 'LocalState', 'Assets')

    return None

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
def copy_files(src_folder_path, dst_folder_path):
    # 确保源文件夹存在
    if not os.path.isdir(src_folder_path):
        print(f"源文件不存在: {src_folder_path}")
        return False

    # 确保目标文件夹存在
    dst_dir = os.path.dirname(dst_folder_path)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # 遍历，并复制文件到目标文件夹
    for filename in os.listdir(src_folder_path):
        src_file_path = os.path.join(src_folder_path, filename)
        dst_file_path = os.path.join(dst_folder_path, filename) + ".jpg"
        print("src_file_path", src_file_path)
        print("dst_file_path", dst_file_path)
        shutil.copy2(src_file_path, dst_file_path)

    return True

# 打开“我的图片_壁纸备份_”
def open_folder(folder_path):
    if os.path.isdir(folder_path):
        os.startfile(folder_path)
    else:
        print(f"指定的路径不是一个有效的文件夹: {folder_path}")


def main():
    source_folder = get_windows11_spotlight_folder()
    dest_folder = os.path.join(get_mypictures_folder(), "_备份壁纸_")
    copy_files(source_folder, dest_folder)
    open_folder(dest_folder)
    return


if __name__ == "__main__":
    main()
