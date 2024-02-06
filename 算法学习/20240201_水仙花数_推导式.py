
def isShuiXianHuaShu(number:int, power:int = 3):
    #digit 数字 digits
    digits = str(number)
    summary = 0
    for i in range(len(digits)):                        #循环，用 number 的长度做循环次数
        summary += int(digits[i])**power                #将 number 的每一位的 power 次方进行累加
    return summary == number

def isShuiXianHuaShu2(number:int, power:int = 3):
    digits = str(number)
    value = [int(digit)**power for digit in digits]     #推导式， digit 是式子中的临时变量
    summary = sum(value)
    return summary == number

def find_narcissistic_numbers(n:int):
    result = []
    for number in range(10**(n-1), 10**n):
        if(isShuiXianHuaShu2(number, n)):
            result.append(number)
    return result

if __name__ == "__main__":
    # 寻找3位数的3次方水仙花数
    result = find_narcissistic_numbers(3)
    print(result)

    # 寻找4位数的4次方水仙花数
    result = find_narcissistic_numbers(4)
    print(result)