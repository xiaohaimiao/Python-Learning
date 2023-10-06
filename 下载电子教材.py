import os
import requests

def DownloadBook(bookId, folder_name, maxCount = 200):
    base_url = f"https://book.pep.com.cn/{bookId}/files/mobile/"

    # 创建文件夹   cvb,
    #Operation System
    os.makedirs(folder_name, exist_ok=True)

    # 遍历图片编号
    for i in range(1, maxCount + 1):
        padded_number = str(i).zfill(3)
        url = f"{base_url}{i}.jpg"
        response = requests.get(url)
        
        if response.status_code == 404:
            print(f"图片 {i}.jpg 不存在，停止抓取")
            break
        elif response.status_code == 200:
            file_path = os.path.join(folder_name, f"{padded_number}.jpg")
            with open(file_path, "wb") as file:
                file.write(response.content)
                print(f"图片 {i}.jpg 已保存", file_path)    
        else:
            print("HTTP 出错了：" + response.status_code)
            
    return 0

bookId = "1212001602145"
bookName = "数学_六年级_上"
#DownloadBook(bookId, bookName)

testUrl = "https://www.runoob.com/python3/python-func-print.html"
response = requests.get(testUrl)
if response.status_code == 200:
    print(response.content)
    html = response.content
else:
    print("出错了：" + response.status_code)