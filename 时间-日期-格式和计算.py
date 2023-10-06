import datetime as dt

birthdayString = input("请输入你的生日八位数：")
birthday = dt.datetime.strptime(birthdayString, "%Y%m%d")
#anyDate = dt.datetime(2012, 5, 23)
anyDate = birthday

print(anyDate.strftime("%Y年%m月%d日") , "是星期：", anyDate.weekday() + 1)
aliveDays = (dt.datetime.today() - anyDate).days
print("距今天数：", aliveDays)
print("距100岁天数：", (dt.datetime(anyDate.year + 100, anyDate.month, anyDate.day) - anyDate).days - aliveDays)
print("距中考天数：", (dt.datetime(anyDate.year + 12, 7, 7) - dt.datetime.today()).days)
deltaTime = (dt.datetime(anyDate.year + 18, 6, 7) - dt.datetime.today())
print("距高考天数：", deltaTime.days)