
# 判断一个数字是否是水仙花数，这里默认按每位上的数字的三次方计算
def isShuiXianHuaShu1(number:int, power:int = 3):
    # 将整数值的 number 转为字符串 digits
    digits = str(number)
    summation = 0    # 这一句可以省略：Python 中不需要定义变量和赋予初始值
    for i in range(len(digits)):       # 循环，用 number 的长度作为循环次数
        item = int(digits[i])**power   # 计算每一位的 power 次方
        summation += item                # 累加

    return summation == number    # 是否是水仙花数

# 判断一个数字是否是水仙花数，这里默认按每位上的数字的三次方计算
def isShuiXianHuaShu2(number:int, power:int = 3):
    # 将整数值的 number 转为字符串 digits
    digits = str(number)

    summation = 0    # 这一句可以省略：Python 中不需要定义变量和赋予初始值
    for digit in digits:           # 迭代 number 的每一位
        item = int(digit)**power   # 计算每一位的 power 次方
        summation += item            # 累加

    return summation == number    # 是否是水仙花数

# 判断一个数字是否是水仙花数，这里默认按每位上的数字的三次方计算
def isShuiXianHuaShu3(number:int, power:int = 3):
    # 将整数值的 number 转为字符串 digits
    digits = str(number)
    # 用推导式生成一个列表，列表中的每个元素是 number 的每一位的 power 次方
    list = [int(digit)**power for digit in digits]     # digit 是式子中的临时变量

    summation = 0    # 这一句可以省略：Python 中不需要定义变量和赋予初始值
    for item in list:           # 迭代列表中的每一个元素，对应 number 的每一位的 power 次方
        summation += item         # 累加

    return summation == number    # 是否是水仙花数

# 判断一个数字是否是水仙花数，这里默认按每位上的数字的三次方计算
def isShuiXianHuaShu4(number:int, power:int = 3):
    digits = str(number)
    list = [int(digit)**power for digit in digits]     #推导式， digit 是式子中的临时变量
    summation = sum(list)         # 用 Python 内置的 sum 函数计算列表中所有元素的和

    return summation == number    # 是否是水仙花数

# 判断一个数字是否是水仙花数：极简版本
def isShuiXianHuaShu5(number:int, power:int = 3):
    return number == sum(int(digit)**power for digit in str(number))

def find_narcissistic_numbers(n:int):
    result = []
    for number in range(10**(n-1), 10**n):
        if(isShuiXianHuaShu3(number, n)):
            result.append(number)
    return result

if __name__ == "__main__":
    # 寻找3位数的3次方水仙花数
    result = find_narcissistic_numbers(3)
    print(result)

    # 寻找4位数的4次方水仙花数
    result = find_narcissistic_numbers(4)
    print(result)