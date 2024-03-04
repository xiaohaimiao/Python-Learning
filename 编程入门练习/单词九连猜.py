import random

s = 9
c = ['sad','days']
j = 0
f = 0
while s > 0:
    r = random.choice(c)
    ch = len(r)
    w = list('?' * ch)
    print('猜猜单词')
    while True:
        n = input('请定义一个分数（输数字，不得小于20，空格退出）')
        if int(n) >= 20:
            break
        else:
            print('输入错误')
            continue  
    print(w)
    d = input('请输入单词（只能输入一个字母，或整个单词。')
    def sh(d3 ,r1 ,w1  ):
        i = 0
        while i < len(r):
            if d == r[i]:
                w[i] = d
                i += 1
        
    if d == ' ':
        print('再见。')
        break
    if d in r:
        sh(d ,r ,w)
        f += 1
    else:
        print('错误')
        s -= 1
    if s == 0:
        print('你失败了！' + str(f))
        d2 = input('是否再来一局？')
        if d2 == '是':
            continue
        else:
            break 
    else:
        if f == n:
            print('你成功了！')
            d2 = input('是否再来一局？')
            if d2 == '是':
                continue
            else:
                break
            
        
        