#import random as r
while True:
    n = input('填写3 - 9之间的数字(含3和9)：')
    n = int(n)
    if n <= 9 and n >= 3 :
        break
    
count = 0
for i in range(1, n + 1):
    for j in range(0, n + 1):
        if i == j: continue
        for k in range(1, n + 1, 2):
            if k == j or k == i or i == j: continue
            #if i == j and k == j : continue
            count += 1
            d = i * 100 + j * 10 + k
            print(str(count).zfill(2), d) 
            #print(str(count).rjust(2, "x"), d) 
            #print(str(count).ljust(2, "x"), d) 
print("共有 " + str(count) + " 种组合。")