def isShuiXianHuaShu(number:int, power:int):
    digits = str(number)
    summary = 0
    for digit in digits:
        summary += int(digit)**power

    return summary == number

def isShuiXianHuaShu2(number:int, power:int):
    digits = str(number)
    list = (int(digit)**power for digit in digits)
    summary = sum(list)
#    if (summary == number):
#        list2 = { int(digit) : int(digit)**power for digit in digits }
#        print(list2, sum(list2))
    return summary == number

def find_narcissistic_numbers(power:int = 3):
    result = []
    for i in range(10**(power - 1), 10**power):
        if isShuiXianHuaShu2(i, power):
            result.append(i)
        
    return result

if __name__ == "__main__":
    n = 3
    resultList = find_narcissistic_numbers(n)
    print("{0}-{1} 之间的水仙花数有：{2}".format(10**(n-1), 10**n, resultList))
    
    n = 4
    resultList = find_narcissistic_numbers(n)
    print("{0}-{1} 之间的水仙花数有：{2}".format(10**(n-1), 10**n, resultList))
