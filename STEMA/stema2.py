#import random as r
while True:
    n = input('填写3 - 9之间的数字(含3和9)：')
    n = int(n)
    if n <= 9 and n >= 3 :
        break
    
count = 0
max = n * 100 + n * 10 + n
for d in range(101, max + 1, 2):
    i = d // 10 // 10
    #j = (d - i*100) // 10
    j = d // 10 % 10
    k = d % 10
    #print(d, i, j, k)

    if i > n or j > n or k > n: continue
    if k == j or k == i or j == i: 
        #print("skip:", d)
        continue
    count += 1
    print(str(count).zfill(2), d) 
print("共有 " + str(count) + " 种组合。")