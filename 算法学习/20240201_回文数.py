import random as r

def isHuiWenShu(n:int):
    string = str(n)
    reverse = int(string[::-1])
    if n == reverse:
        return True
    else:
        return False

if __name__ == "__main__":
    for i in range(10):
        n = r.randint(100, 10000)
        message = "是" if isHuiWenShu(n) else "不是"
        #message = isHuiWenShu(n) ? "是" : "不是"
        print("数字 {0} {1} 回文数。".format(n, message))
    