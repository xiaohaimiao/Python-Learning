# 生成斐波那契数列并显示
# 生成斐波那契数列    
def fib(count):
    result = []
    last0 = 0
    last1 = 1
    for i in range(count):
        now = last0 + last1
        last0 = last1
        last1 = now
        result.append(now)
    return result

r = input('输入要生成的数的数量（默认为10）：')
if r == "":
    count = 10
else:
    count = int(r)

fibs = fib(count)
i = 0
for fib in fibs:
    i += 1
    print(str(i).rjust(3, '0'), fib)
    
print()

for i in range(len(fibs)):
    print(str(i + 1).rjust(3, '0'), fibs[i])

