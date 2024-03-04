import snoop

@snoop
def Euclidean(max:int, min:int):
    if min > max:
        min, max = max, min
    yu = max % min
    if yu == 0:
        return min
    return Euclidean(min, yu)

@snoop
def Euclidean2(max:int, min:int):
    if min > max:
            min, max = max, min
    while True:
        yu = max % min
        if yu == 0:
            return min
        max, min = min, yu
    return

if __name__ == "__main__":
    a = 54
    b = 12
    zuiDaGongYinShu = Euclidean(a, b)
    zuiDaGongYinShu = Euclidean2(a, b)
    print(a, b, '的最大公因数数是：', zuiDaGongYinShu)