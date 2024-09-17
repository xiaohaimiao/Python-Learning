# 一个可以获取指定城市的天气信息的程序

# 版本：V1.0
# 主要功能：
# 可以从“和风”网站获取指定城市的天气信息
# 步骤：
# 1. 使用key调出网站的API
# 2. 获取指定城市名和行政编码以及目标日期
# 3. 通过API获取天气信息，并保存到数据文件
# 4. 输出结束信息

# 版本记录：
#   1.1    2024/09/17   增加了读写缓存的功能
#   TODO: 1.2
#   TODO: 1.x

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MyCode import print_error, run_by_default_app, print_color
import datetime as DateTime
import requests

def make_folder(new_folder_name, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        # 获取文件夹父目录路径
        parent_folder_path = os.path.dirname(folder_path)
        # 创建新文件夹路径
        new_folder_path = os.path.join(parent_folder_path, new_folder_name)
        # 重命名文件夹
        try:
            os.rename(folder_path, new_folder_path)
        except Exception as e:
            print("Error:", e)
    return

# 获取指定地点的行政编码
def get_location_id(location_string, location_adm, API_key):
    url = f"https://geoapi.qweather.com/v2/city/lookup?location={location_string}&adm={location_adm}&range=cn&key={API_key}"
    json = get_API(url)
    if json != None and json["code"] == "200":
        return json["location"][0]["id"], json["location"][0]["name"], json["location"][0]["adm1"], json["location"][0]["adm2"]
    return None, None, None, None


# 获取指定行政编码的未来三日的天气预报
def get_weather_info_by_api(location_id, API_key):
    url = f"https://devapi.qweather.com/v7/weather/3d?location={location_id}&key={API_key}"
    json = get_API(url)
    today = DateTime.date.today().strftime('%d/%m/%Y')
    if json != None:
        write_weather_info_into_cache(json, today)
        return json["daily"]
    return None

def read_weather_info_into_cache(city_id, city_name, date:DateTime):
    # 构造缓存文件的文件名
    cache_filename_path = gouzao_city_cache_file_name(city_id, city_name, date)
    if not os.path.exists(cache_filename_path):
        return None
    # 读取文件
    with open(cache_filename_path, "r") as file:
        json_data = file.read()
    
    return json_data

#
def write_weather_info_into_cache(weather_info_folder, city_id, city_name, date:DateTime, weather_data):
    # 构造缓存文件的文件名
    cache_filename_path = gouzao_city_cache_file_name(weather_info_folder, city_id, city_name, date)
    # 写入文件（覆盖已有文件）
    with open(cache_filename_path, "w") as file:
        file.write(weather_data)
    return

def gouzao_city_folder_path(weather_info_folder, city_id, city_name):
    city_folder_name = f"{city_id}_{city_name}"
    city_folder_path = os.path.join(weather_info_folder, city_folder_name)
    # 确保文件夹存在，不存在就创建
    if not os.path.exists(city_folder_path):
        os.makedirs(city_folder_path)
    return city_folder_path

def gouzao_city_cache_file_name(weather_info_folder, city_id, city_name, date:DateTime):
    city_folder_path = gouzao_city_folder_path(weather_info_folder, city_id, city_name)
    # 获取时间
    date_string = date.strftime("yyyy-MM-dd")
    # 构造缓存文件的的完整路径
    cache_filename = f"{date_string}.json"
    return os.path.join(city_folder_path, cache_filename)

def get_API(url):
    response = requests.get(url)
    print(url)
    if response.status_code == 200:
        json = response.json()
        return json
    else:
        print_error(f'请求失败，状态码：{response.status_code}')
    return None

# 输出天气预报信息
def print_weather_info(location_id, location_name, weather_info, location_adm1 = ""):
    print(f"{location_id} {location_adm1} {location_name} 未来三日天气预报：")
    for day_weather_info in weather_info:
        print_color(f'\t{day_weather_info["fxDate"]}', "bright_green")
        print_color(f'\t\t最低温度：{day_weather_info["tempMin"]} 最高温度：{day_weather_info["tempMax"]}', "bright_yellow")
        print_color(f'\t\t日间：{day_weather_info["textDay"]} 夜间：{day_weather_info["textNight"]}', "bright_green")
    return


def main():
    # script：脚本
    _script_folder_path_ = ""
    location_string = "lijiang"
    location_adm = ""
    if len(sys.argv) > 1:
        location_string = sys.argv[1]
        if len(sys.argv) > 2:
            location_adm = sys.argv[2] 
    else:
        print_error("请提供有效城市名和上级城市名")
        #sys.exit(1)
        
    API_key = "4221343812994b3db7eb5cc3bb6e252f"
    # 获取用户提供的地点的行政编码
    location_id, location_name, location_adm1, location_adm2 = get_location_id(location_string, location_adm, API_key)
    if not location_id:
        print_error(f"获取地点信息失败：{location_string} {location_adm}")
        return
    
    # 子文件夹相关处理...
    # 默认为脚本所在目录下的 "xxxx" 子目录，如果用户提供参数则以用户指定的为父目录
    weath_info_cache_folder =  ""
    # 获取指定行政编码的未来三日的天气预报
    # 读取天气信息的缓存
    weather_info = ""
    if weather_info == None:
        # 没有缓存，需要调用 API
        weather_info = get_weather_info_by_api(location_id, API_key)
        if weather_info == None:
            print_error(f"获取天气预报信息失败：{location_id} {location_name}")
            return
        # 写入缓存
        date_time = DateTime.date.today().strftime('%d/%m/%Y')
        write_weather_info_into_cache(weath_info_cache_folder, location_id, location_name, date_time, weather_info)

    # 输出天气预报信息
    print_weather_info(location_id, location_name, weather_info, location_adm1)
    return


if __name__ == "__main__":
    main()
