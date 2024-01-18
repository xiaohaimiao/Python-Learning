list = [13, 7, 4, 8, 5, 2, 3, 10, 11, 9, 17, 6]
length = len(list)
for i in range(length - 1):
    for j in range(length - 1, i, -1):
        a = list[j]
        b = list[j - 1]
        if b > a:
            list[j] = b
            list[j - 1] = a
            print((i,j), str(a).ljust(2, ' ') + ' <  ' + str(b).ljust(2, ' '), list)
        else:
            print((i, j), str(a).ljust(2, ' ') + ' >= ' + str(b).ljust(2, ' '), list)
    print(list, '\r\n')