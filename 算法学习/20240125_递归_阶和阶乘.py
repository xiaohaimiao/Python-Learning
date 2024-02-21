def jieHe(n):
    summation = 0
    for i in range(1, n + 1):
        summation += i
    return summation

def jieHe2(n):
    if n <= 0:
        return 0
    return jieHe2(n - 1) + n

def jieHe3(n, sum = 0):
    if n <= 0:
        return 0
    jiehe = jieHe3(n - 1, sum)
    sum = jiehe + n
    return sum

def jieCheng2(n):
    if n <= 1:
        return 1
    return jieCheng2(n - 1) * n           

def jieCheng(n):
    summation = 1
    for i in range(1, n + 1):
        summation *= i
    return summation

n = 100
print(str(n) + " 的阶和：", jieHe3(n))
print(str(n) + " 的阶乘：", jieCheng2(n))

