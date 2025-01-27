# 拆分动态照片
# 步骤：
# 1.用二进制打开指定文件
# 2.找到其中视频文件的开头标识
# 3.以标识位置为线将文件拆分
# 4.将拆分后的两部分数据以约定名称保存到指定文件的目录
# 版本：
# V1.1   支持命令行参数：指定文件或文件夹（默认当前文件夹的所有动态照片）
# V1.2   兼容各品牌手机的“动态照片”格式：识别图片结束标识、视频开始标识（丢弃之间的部分）——防通用，顺带记录了一些信息
#TODO: V1.3  如果指定的参数不是文件而是目录，则对目录中所有动态照片进行拆分
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MyCode import print_error, run_by_default_app, print_color

def get_file_path():
    if len(sys.argv) < 2:
        print_error("请提供目标文件名或完整路径")
        script_name = os.path.basename(__file__)
        script_name = os.path.basename(sys.argv[0])
        print_color(f"{script_name} <目标文件名>")
        return None
    file_path = sys.argv[1]
    if not (os.path.isdir(file_path) and file_path.endswith(".jpg")):
        print_error(f"请提供有效的 JPG 文件：'{file_path}'")
        return None
    # 确保文件路径为绝对路径 
    file_path = os.path.abspath(file_path)
        
    return file_path

def find_marker_and_split_file(file_path):
    # 检查参数是否有效
    if not (os.path.isdir(file_path) and file_path.endswith(".jpg")):
        return None, f"参数错误：不是有效的 JPG 文件：'{file_path}'"
    
    # 打开图片文件，读取内容 
    with open(file_path, "rb") as file:
        content = file.read()
    # 查找 jpg 的结束标志
    jpg_keywords = b"\xFF\xD9\x00\x00" #图片内容结束标识
    jpg_position = content.find(jpg_keywords)
    if jpg_position == -1:
        return None, f"没有找到图片内容结束标识：'{file_path}'"
    
    # 查找视频的开头标记 Marker
    mp4_keywords = b"\x00\x00\x00\x18\x66\x74\x79\x70" #视频内容开头标识
    mp4_position = content.find(mp4_keywords)
    if mp4_position == -1:
        return None, f"没有找到视频内容开头标识：'{file_path}' "
    # 分别保存两个文件并重命名
        # 保存为图片文件：源文件名加后缀 _Photo.jpg
        # 1. 源文件路径 dirname + basename.splitext[-2] + "_Photo.jpg" 
        # 2. 源文件路径 替换 ".jpg" 为 "_Photo.jpg"
    jpg_file_path = file_path.lower().replace(".jpg", "_Photo.jpg")
    with open(jpg_file_path, "wb") as file:
        # 注意：保存的位置要包含标识本身
        file.write(content[:jpg_position + len(jpg_keywords)]) 
        
        # 保存为视频文件
    mp4_file_path = file_path.lower().replace(".jpg", "_Movie.mp4")
    with open(mp4_file_path, "wb") as file:
        file.write(content[mp4_position:])
    
    return jpg_file_path, mp4_file_path

def main():
    working_folder = os.curdir
    script_folder = __file__
    print(f"working_folder: {working_folder} \n\t {os.path.abspath(working_folder)}")
    print(f"script_folder: {script_folder}")
    print(f"script_folder: {sys.argv[0]}")
    
    
    # 1.用二进制打开指定文件
    file_path = get_file_path()
    if file_path is None:
        return False
    # 2.找到其中视频文件的开头标识
    # 3.以标识位置为线将文件拆分
    jpg_file_path, mp4_file_path = find_marker_and_split_file(file_path)
    if jpg_file_path is None:
        print_error(f"错误：{mp4_file_path}")
        return False
    
    # 4.将拆分后的两部分数据以约定名称保存到指定文件的目录
    if run_by_default_app(jpg_file_path):
        print_color("成功!")
    return True

if __name__ == "__main__":
    main()
    