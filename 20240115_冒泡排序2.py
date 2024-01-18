import random

# 创建随机整数列表
def creat_random_int_list(min, max, length):
    # min 最小，max 最大 
    # start 开始，stop/end 停止/结束
    # top 最高, low/bottom 底部
    list = []
    for i in range(length):
        list.append(random.randrange(min, max + 1))
    return

list = creat_random_int_list(100, 200, 10)
def sort(list):
    length = len(list)
    for i in range(length - 1):
        for j in range(length - 1, i -1):
            a = [j]
            b = [j -1]
            if a > b:
                list[j] = b
                list[j - 1] = a
    return list
list = sort(list)
print(str(list))