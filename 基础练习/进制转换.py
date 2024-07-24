def dec2Binary1(n:int) -> str:
    n = int(n)
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    return result

def dec2Binary2(n:float, jingdu:int = 6) -> str:
    n = n - int(n)          # 去掉整数部分
    n = round(n, jingdu)    # 保留指定精度的小数部分
    result = ""
    while n > 0:
        n = n * 2
        gewei = int(n)    # 仅保留整数部分
        result = result + str(gewei) 
        n = n - gewei       # 去掉整数部分
    return result

# 将十进制数转换为二进制
def dec2Binary(n:float, jingdu:int = 6) -> str:
    result = ""
    # 拆分 number 为整数与小数
    zhengShu = int(n)
    #zhengShu = n // 1
    xiaoShu = n % 1
    #zhengShu, xiaoShu = divmod(n, 1)
    
    # 调用 toBinary1
    result1 = dec2Binary1(zhengShu)
    
    # 调用 toBinary2
    result2 = dec2Binary2(xiaoShu, jingdu)
        
    # 拼接结果
    if len(result2) == 0:
        result = result1
    else:
        result = result1 + '.' + result2
    
    return result   

def binary2Dec(bin:str) -> int:
    result = 0
    i = len(bin) - 1
    for char in bin:
        result += int(char) * 2 ** i
        i -= 1
        
    return result

def oct2Dec(oct:str) -> int:
    result = 0
    i = len(oct) - 1
    for char in oct:
        result += int(char) * 8 ** i
        i -= 1
        
    return result

def hex2Dec(hex:str) -> int:
    result = 0
    hex = hex.upper()
    i = len(hex) - 1
    for char in hex:
        if char >= 'A' and char <= 'F' :
            digital = ord(char) - 55
        else:
            digital = int(char)
        
        result += digital * 16 ** i
        i -= 1
        
    return result

number = 12345
result = dec2Binary(number)
#print(number, result, binary2Dec(result))
print(oct2Dec("123"))
print(hex2Dec("1aF3"))
