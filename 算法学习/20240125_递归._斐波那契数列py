# 生成斐波那契数列——递推法
def fib(n):
    result = []
    last1 = 0
    last2 = 1
    for i in range(n):
        now = last1 + last2
        last1 = last2
        last2 = now
        result.append(now)
    return result

def fib2(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fib2(n-1)
        fib = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(fib)
        print(n, fib_seq)
        return fib_seq

def fib3(n, cache={}):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        if n in cache:
            return cache[n]
        else:
            fib_seq = fib3(n-1, cache)
            fibn = fib_seq[-1] + fib_seq[-2]
            fib_seq.append(fibn)
            print(n, cache)
            cache[n] = fib_seq
            return fib_seq

n = 10
print("递归：", fib3(n))
print()
"""
for i in range(len(fibs)):  # 枚举 range(n) 中的每一项
    print(str(i + 1).rjust(3, '0'), fibs[i])
"""
