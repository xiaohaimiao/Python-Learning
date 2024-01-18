import random
import snoop

# 调试模式
isDebug = True

def debug(message):
    if isDebug:
        print(message)
    return

# 创建随机整数列表
def Creat_Random_Int_List(min, max, length):
    # min 最小，max 最大 
    # start 开始，stop/end 停止/结束
    # top 最高, low/bottom 底部
    list = []
    for i in range(length):
        list.append(random.randrange(min, max + 1))
    return list

# 选择排序：每轮比较后交换
def SelectionSort(list):
    debug("选择排序：")
    length = len(list)
    for i in range(length - 1):
        maxIndex = i
        for j in range(i + 1, length):
            if list[j] > list[maxIndex]:
                maxIndex = j
        list[i], list[maxIndex] = list[maxIndex], list[i]

        debug(str(i) + "\t" + str(list))
    return list

# 选择排序：每次比较交换，效率低
#@snoop
def SelectionSort_Swap(list):
    debug("\r\n选择排序2：")
    length = len(list)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]
        debug(str(i) + "\t" + str(list))
    return list

# 测试代码
unSortList = Creat_Random_Int_List(100, 200, 10)
print("UnSort:", unSortList)

SortedList  = SelectionSort(unSortList.copy())
print("Sorted:", SortedList)

SortedList  = SelectionSort_Swap(unSortList.copy())
print("Sorted:", SortedList)
