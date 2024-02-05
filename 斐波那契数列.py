# 生成斐波那契数列并显示
# 生成斐波那契数列    
def fib(count):
    result = []
    last1 = 0
    last2 = 1
    for i in range(count):
        now = last1 + last2
        last1 = last2
        last2 = now
        result.append(now)
    return result

r = input('输入要生成的数的数量（默认为10）：')
if r == "":
    count = 10
else:
    count = int(r)

fibs = fib(count)
i = 0
for fib in fibs:    # 枚举 fibs 中的每一项
    i += 1
    print(str(i).rjust(3, '0'), fib)
    
print()
"""
for i in range(len(fibs)):  # 枚举 range(n) 中的每一项
    print(str(i + 1).rjust(3, '0'), fibs[i])
"""
