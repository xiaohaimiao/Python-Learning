def YangHuiSanJiao(count):
    result = []
    for i in range(count):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
    return result


sanJiao = YangHuiSanJiao(10)

for row in sanJiao:
    print(row)