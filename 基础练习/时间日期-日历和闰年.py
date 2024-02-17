import datetime as dt

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def IsRunYear(year):
    if float(year // 4) == year / 4:
        if year % 100 == 0:
            if year % 400:
                return True
            else:
                return False
        else:
            return True
        
    return False

year = int(input('请输入年份（四位数字）：'))
isRunYear = IsRunYear(year)
if isRunYear:
    print(year, '是闰年')
else:
    print(year, '是平年')
    
for month in range(0 , 2):
    print(month + 1, ":")
    if month + 1 == 2 and isRunYear:
        lastDay = days[month] + 1
    else:
        lastDay = days[month]
    for day in range(0, lastDay):
        print(" " + str(day + 1), end = "")
    print("\n")
