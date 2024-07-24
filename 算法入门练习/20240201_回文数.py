import random as r

def isHuiWenShu(n:int):
    digits = str(n)
    reverse = digits[::-1]
    return n == int(reverse)


def isHuiWenShu21(n:int):
    digits = str(n)
    digitsList = list(digits)
    reverseList = digitsList.reverse()

    return digitsList == reverseList

def isHuiWenShu2(n:int):
    digits = str(n)
    
    digitsList = []
    length = len(digits)
    #for digit in digits:
    #    digitsList.insert(0, digit)
        
    for i in range(length):
        digitsList.append(digits[length-i-1])
        
    reverseList = "".join(digitsList)
    return n == int(reverseList)

def isHuiWenShu3(n:int):
    string = str(n)
    length = len(string)
    for i in range(length//2):
        digit1 = string[i]
        digit2 = string[length-i-1]
        if digit1 != digit2:
            return False
    return True

def qiuDiJiWei(n:int, pos:int):
    if(pos < 1):
        print("POS 参数错误：", pos)
        return 0
    x = n // 10**(pos-1) % 10
    return x

def isHuiWenShu4(n:int):
    string = str(n) 
    length = len(string)
    for i in range(length//2): # 这里有优化
        digit1 = qiuDiJiWei(n, i+1)
        digit2 = qiuDiJiWei(n, length-i)
        #print(n, i, digit1, digit2, length)
        #print(char1, char2)
        if digit1 != digit2:
            return False
    return True

# 基于第4种方法的变体        
def isHuiWenShu5(number:int):
    if number < 0:
        return False
    temp = number
    palindromeNum = 0
    while temp != 0:
        palindromeNum = palindromeNum*10 + temp%10
        temp //= 10
    return palindromeNum == number

if __name__ == "__main__":
    for i in range(10):
        n = r.randint(100, 10000)
        message = "是" if isHuiWenShu4(n) else "不是"
        #message = isHuiWenShu(n) ? "是" : "不是"
        print("数字 {0} {1} 回文数。".format(n, message))
    
    result = []
    for i in range(1000, 10000):
        if isHuiWenShu5(i):
            result.append(i)
    print("回文数:", result)
    
    #print(12321, isHuiWenShu4(12321))
