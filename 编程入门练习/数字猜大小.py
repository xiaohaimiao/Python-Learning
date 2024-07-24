import random
import time

def showMessage(messageA, messageB):
    #获取系统时间
    timeString = time.strftime("[%H:%M:%S]", time.localtime(time.time()))
    print(timeString + "\t" + messageA + str(messageB));

while True:
    s = input('你猜是大还是小（回车退出）')
    if s == '':
        print('下次再见')
        break
    r = random.randint(0,1000000000000000000)
    if r >= 500000000000000000 and s == '大' or r < 500000000000000000 and s == '小':
        showMessage('正确：', r)
    else:
        showMessage('错误: ', r)
