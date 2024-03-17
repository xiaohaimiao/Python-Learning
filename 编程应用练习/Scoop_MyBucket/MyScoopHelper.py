import argparse
import json
import os
import subprocess
import requests
import hashlib
from tqdm import tqdm
import re

# Scoop Main Bucket 的 URL
# https://raw.githubusercontent.com/ScoopInstaller/Main/master/bucket/7zip.json
MAIN_BUCKET_URL = 'https://raw.githubusercontent.com/ScoopInstaller/Main/master/bucket/'
# 缓存目录和 Bucket 目录
CACHE_DIR = '_MyBucket_Cache_'
BUCKET_DIR = '_MyBucket_'

currentDir = os.path.abspath(__file__)
CACHE_DIR = os.path.join(os.path.dirname(currentDir), CACHE_DIR)
BUCKET_DIR = os.path.join(os.path.dirname(currentDir), BUCKET_DIR)

def download_json(package):
    # 如果 json 文件不存在，下载 json 文件
    json_path = os.path.join(BUCKET_DIR, package + '.json')
    if os.path.exists(json_path):
        # TODO: json 文件存在，则比较版本信息，以确认是否更新
        os.remove(json_path) # 删除旧版本的 json 文件
    
    """下载 Scoop Main Bucket 的 json 文件"""
    url = MAIN_BUCKET_URL + package + '.json'
    response = requests.get(url, proxies={'http': 'http://127.0.0.1:10809', 'https': 'http://127.0.0.1:10809'})

    print(f"*** 下载 {package}.json\t{url}")
    # 如果下载成功
    if response.status_code == 200:
        with open(os.path.join(BUCKET_DIR, package + '.json'), 'w') as json_file:
            json_file.write(response.text)
        print(f"\t*** 下载 {package}.json 完成。")
    else:
        print(f"\t---下载 {package}.json 失败。")
    return

def get_download_url(package):
    """获取下载链接"""
    json_path = os.path.join(BUCKET_DIR, package + '.json')
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
    url = data['architecture']['64bit']['url']
    hash = data['architecture']['64bit']['hash']
    return data, url, hash

def validate_file_hash(file_path, hash):
    """校验文件哈希值"""
    if not os.path.exists(file_path):
        return False
    with open(file_path, 'rb') as file:
        data = file.read()
        file_hash = hashlib.sha256(data).hexdigest()
    return file_hash == hash

def try_download_package(package):
    """下载包并更新 json 文件"""
    data, url, hash = get_download_url(package)
    # 'https://github.com/git-for-windows/git/releases/download/v2.44.0.windows.1/PortableGit-2.44.0-64-bit.7z.exe#/dl.7z'
    # 如果包含 #/，则只下载 #/ 前面的部分
    if '#/' in url:
        filename = url.split('#/')[0]
        filename = filename.split('/')[-1]
    else:
        filename = url.split('/')[-1]
    file_path = os.path.join(CACHE_DIR, filename)
    # 文件存在且校验 Hash 值一致
    if validate_file_hash(file_path, hash):
        print(f"\033[32m*** 本地文件 {file_path} 已存在，无需下载。\033[0m")
    else:
        # 下载文件
        print(f"\033[34m*** 下载文件 {filename}： {url}\033[0m")
        result = subprocess.run(
            ['D:\\_Dev_\\_Scoop_\\apps\\aria2\\current\\aria2c.exe', 
             '-x10', '-s10', '-j10', '-d', CACHE_DIR, 
             '--all-proxy=http://127.0.0.1:10809', url],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # 显示下载进度
        if result.returncode == 0:
            with tqdm(total=100, unit='%', ncols=80, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
                lines = result.stdout.decode().splitlines()
                for line in lines:
                    # '[#1c71ee 1.3MiB/1.8MiB(75%) CN:1 DL:449KiB ETA:1s]'
                    match = re.search(r'\((\d+)%\)', line)
                    if match:
                        progress = match.group(1)
                        pbar.update(float(progress))
                        
            print(f"\n\r\033[34m\t*** 下载完成：{filename}： {file_path}\033[0m")
        else:
            print(f"\n\r\033[31m\t--- 下载失败：{filename}\033[0m")
    return
        
def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='下载 Scoop 包')
    parser.add_argument('file', help='包含包名的文件', default='packages.txt', nargs='?')
    args = parser.parse_args()

    # 创建缓存目录和 Bucket 目录
    os.makedirs(CACHE_DIR, exist_ok=True)
    os.makedirs(BUCKET_DIR, exist_ok=True)    
    
    # 读取文件中的包名
    if os.path.isabs(args.file):
        file_path = args.file
    else:
        script_dir = os.path.dirname(currentDir)
        file_path = os.path.join(script_dir, args.file)
    
    with open(file_path, 'r') as file:
        packages = [line.strip() for line in file]

    # 对于每个包，下载 json 文件
    for package in packages:
        download_json(package)
            
    # 下载包
    for package in packages:
        try_download_package(package)

if __name__ == '__main__':
    main()
