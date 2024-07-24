import datetime as dt
import random as r
import string

# 生成随机密码
def randomPassword():
    x = ['sleepy', 'sad', 'happy', 'green', 'hot', 'cold', 'yellow', 'cloudy']
    m = ['apple', 'dog', 'cap', 'cat', 'tomato', 'potato']
    n = r.randrange(0, 100)
    y = r.choice(string.punctuation)
    x = r.choice(x)
    m = r.choice(m)
    return x + m + str(n) + y

# 生成学生 ID 和 密码的内容
def makeStudentsInfo():
    students = []
    today = dt.datetime.today()
    for day in range(1, today.day + 1):
        date = dt.datetime(today.year, today.month, day)
        id = date.strftime("%Y%m%d")        # 注意：ID 必须为数字
        passWord = randomPassword()         # 注意：密码必须为文本、数字和可见字符，不能有 ','
        student = { "ID" : id, "Password": passWord, "成绩": {"一年级": {"语文":"99.5", "数学":"100"},  }}
        students.append(student)
    return students

# 将学生信息写入文本文件
def writeStudentsInfo2File(filename, students):
    file = open(mode="w", file=filename)
    text = ""
    for student in students:
        line = student["ID"] + "," + student["Password"]
        text += line + "\n"

    file.write(text)
    file.close()
    return file.name

# 从文件读取学生信息
def readStudentsInfoFromFile(filename):
    lineNumber = 0
    studentList1 = []                   # 初始化列表1
    studentList2 = []                   # 初始化列表2
    # context = filename + "文件内容：\n"
    text = "{}文件内容：\n".format(filename)
    
    file = open(mode="r", file=filename)
    for line in file:
        lineNumber += 1
        text += line                    # 保存到 text 变量，以便返回
        line = line.rstrip('\n')        # 去掉行尾的 \n
        data = line.split(",")          # 以 ',' 为分隔符，拆分为字符串数组
        student1 = (data[0], data[1])   # 将每一行数据保存为【元组】
                                        # 访问元组的数据项，用【数字下标】
        studentList1.append(student1)   # 添加到列表1 列表.append()
        student2 = {"ID": data[0], "Password": data[1]} # 将每一行数据保存为【字典】项
                                        # 访问【字典】项的数据项，用【名字下标】Key
        studentList2.append(student2)   # 添加到列表2 列表.append()
        # print("[" + str(lineNumber).rjust(3, "0") + "]", line, end = "")
    file.close()
    return text, studentList1, studentList2

# 主程序代码
filename = "test.txt"

writeStudentsInfo2File(filename, makeStudentsInfo())
# result “结果”
result = readStudentsInfoFromFile(filename) # 接收返回值，是个元组。
print(result[0])
students1 = result[1]
#print(students1)
students2 = result[2]
#print(students2)

# 在返回值中搜索需要的内容
# 注意：元组和字典的区别——元组（有序）用【数字下标】，字典（无序）用【名字下标】不能用【数字下标】
for student in students1:
    if student[0] == '20230815':    # 元组（有序）用【数字下标】
        print(student)
        break

for student in students2:
    if student["ID"] == '20230816': # 字典（无序）用【名字下标】不能用【数字下标】
        print(student)
        break
