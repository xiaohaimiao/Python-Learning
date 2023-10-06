import random   #引入
import string
while True:
    def one():  #建立函数
        n = ['伤心的','悲伤的','开心的','欢快的','痛苦的','激动的']
        x = ['小明','蜜蜂','猫','狗','小仓鼠','隔壁老王']
        m = ['在操场上的','在卫生间里的','在屋顶上的','在教室里的','在泳池里的','在餐馆里的','在公园里的','在垃圾堆里的','图书馆里的']
        y = ['篮球架上','讲台上','饭桌前','花洒旁','化石旁','马桶上','乒乓球桌前','兵马俑前','棺材里','船上','床上','电脑前']
        z = ['睡觉','唱歌','跳芭蕾舞','跳踢踏舞','跳街舞','打乒乓球','洗澡','游泳','看电视','玩毛线球','采蜜','跑步','翻墙','飞来飞去','演讲']  #建造列表
        x = random.choice(x)
        m = random.choice(m)
        n = random.choice(n)
        y = random.choice(y)
        z = random.choice(z)    #随即从列表中取一项
        print("\r\n笑话：" + x + m + y + n + z) #组成笑话
        return(True)    #习惯
        
    def two():
        x = ['sleepy','sad','happy','green','hot','cold','yellow','cloudy']
        m = ['apple','dog','cap','cat','tomato','potato']
        n = random.randrange(0,100)
        y = random.choice(string.punctuation)   #随机从标点库中取一项
        x = random.choice(x)
        m = random.choice(m)
        print("\r\n密码：" + x + m + str(n) + y)#组成密码
        return(True)
        
    j = [1, 2, 3, 2, 3, 1, 3, 3, 2, 3, 3, 3, 2, 3, 1]  #建一个列表，用来做抽中不同奖项的概率
    m = random.choice(j)
    if m == 1:  #如果中1，执行函数one
        one()
    elif m == 2:    #否则如果中2，执行函数two
        two()
    else:       #否则（也就是中3）打印“谢谢惠顾”
        print('谢谢惠顾')
    i = input('还抽吗？ n\y')
    if i == 'n':
        continue
    else :
        break
    