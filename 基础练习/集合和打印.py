import datetime as DateTime
def r(d):
    z = ['周一','周二','周三','周四','周五','周六','周日']
    z2 = z(d)
l = ['22','3','4']
x = '555'
y1 = ('345',l,x)
y = ('123',l,x,y1)
scores = { "Name":"A", "语文": 94, "数学":93.5, "英语":99}

#print(l , x , y1 , y, sep="\n")

student1 = ("Student1", 94, 93.5, 99)
student2 = ("Student2", 94, 93.5, 99)
student3 = ("Student3", 94, 93.5, 99)
student1List = ["Student1", 94, 93.5, 99]
student1Set = {"Student1", 94, 93.5, 99}
studentDicItem1 = { "Name":"Student1", "语文": 94, "数学":93.5, "英语":99}
studentDicItem2 = { "Name":"Student2", "语文": 94, "数学":93.5, "英语":99}
studentDicItem3 = { "Name":"Student3", "语文": 94, "数学":93.5, "英语":99}

studentsList = [
    studentDicItem1,
    studentDicItem2,
    studentDicItem3,
]
studentsList2 = [
    student1,
    student2,
    student3,
]
time = DateTime.datetime.now()
timeStr = TimeFormat(time) #strftime("%Y年%m月%d日周%w %H:%M:%S")
i = 0
print("包含字典的列表：")
for student in studentsList:
    i += 1
    print("[" + timeStr + "]", i, ">", student)
    for name in student:
        print("\t", name, "=", student[name])

print("名为 'Student1' 的数据：")
for student in studentsList:
    if student["Name"] == "Student1" :
        print(student)

i = 0    
print("包含元组的列表：")
for student in studentsList2:
    i += 1
    print(i, ">", student)
    for value in student:
        print("\t", value)

print("名为 'Student1' 的数据：")
for student in studentsList2:
    if student[0] == "Student1" :
        print(student)
    