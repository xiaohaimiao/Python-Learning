def isSafe(qiPang, position):
    x = position[0]
    y = position[1]
    value = qiPang[x][y]  
    if value == 0:
        # 对相关位置标记
        for i in range(8):
            for j in range(8):
                a, b = i - x, j - y
                if (a, b) == (0, 0):
                    qiPang[i][j] = 1
                elif a == 0:
                    qiPang[i][j] = -1                    
                elif b == 0:
                    qiPang[i][j] = -1
                elif a + b == 0 or a == b:
                    qiPang[i][j] = -1
        # 执行动作：标记皇后位置
        qiPang[x][y] = 1 
        print("Safe:",position, "value = ", value)
        return True
    else:    
        #print("Not safe:",position, "value = ", value)
        return False

def printMap(qiPang):
    for i in qiPang:
        print(i)

def eight_queens_ditui(qiPang):    
    for i in range(8):
        for j in range(8):
            if isSafe(qiPang, (i, j)):
                print(f"皇后：{i},{j}")
    return

def eight_queens_digui(qiPang, position):
    x = position[0]
    y = position[1]
    # 判断参数是否有效
    rows = len(qiPang)
    cols = len(qiPang[0])
    
    if rows != 8 or cols != 8:
        print("失败：", str(position))
        return False
    if x <= -1 or y <= -1:
        print("失败：", str(position))
        return False
    if x >= 8 or y >= 8:
        print("失败：", str(position))
        return False

    value = qiPang[x][y]
    if value == 1:
        print("失败：", str(position))
        return False
    if value == -1:
        print("失败：", str(position))
        return False
    if isSafe(qiPang, position):
        print("成功：", str(position))
        return True
    if eight_queens_digui(qiPang, (x + 1, y)):
        return True
    if eight_queens_digui(qiPang, (x - 1, y)):
        return True
    if eight_queens_digui(qiPang, (x, y + 1)):
        return True
    if eight_queens_digui(qiPang, (x, y - 1)):
        return True
    return False

def clean(qiPang):
    for i in range(8):
        for j in range(8):
            if qiPang[i][j] == -1:
                qiPang[i][j] = 0


if __name__ == "__main__":
    qiPang = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    #qiPang = [[0] * 8] * 8
    print(qiPang)
    start = (0, 0)
    '''for x in range(8):
        for y in range(8):
            if eight_queens_ditui(qiPang, x, y):
                print("成功：", x, y)
                printMap(qiPang)
                break 
            else:
                print("失败：", x, y)'''
                
    #eight_queens_digui(qiPang, start)
    eight_queens_ditui(qiPang)
    clean(qiPang)
    printMap(qiPang)