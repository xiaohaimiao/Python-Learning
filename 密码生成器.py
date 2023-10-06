import string
import random
while True:
    x = ['sleepy','sad','happy','green','hot','cold','yellow','cloudy']
    m = ['apple','dog','cap','cat','tomato','potato']
    n = random.randrange(0,100)
    y = random.choice(string.punctuation)
    x = random.choice(x)
    m = random.choice(m)
    print("\r\n密码：" + x + m + str(n) + y)
    e = input('是否继续生成密码？（y/n）')
    if e == 'y':
        continue
    else:
        print('再见。')
        break
    