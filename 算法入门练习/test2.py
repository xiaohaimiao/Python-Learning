def Hanoi(level:int, x:int, y:int):
    if level > 1:
        Hanoi(level - 1, x, 6-x-y)
    print(str(level) + "号从柱子" + str(x) + "移动到柱子" + str(y))
    if level > 1:
        Hanoi(level - 1, 6-x-y, y)
    return

if __name__ == '__main__':
    x = Hanoi(5, 3, 1)
else:
    print(f"__name__ == {__name__}")