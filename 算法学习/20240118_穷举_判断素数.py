#2024/1/18
import math

def IsPrime(n:int):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        #if n // i == n / i:
        if n % i == 0:
            #print(i)00
            0.
            return False

    return True

prime = []
notPrime = []
for i in range(1, 100 + 1):
    if IsPrime(i):
        prime.append(i)
    else:
        notPrime.append(i)
print("素数：", prime)
print("不是素数：", notPrime)
