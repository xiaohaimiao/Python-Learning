def generate_pascal_triangle(rows):
    result = []
    #result.append([1])
    for i in range(rows):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1 , i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
    return result

#count = str(input('输入要生成的行数'))
count = 10
result = generate_pascal_triangle(count)
for row in result:
    print(row)