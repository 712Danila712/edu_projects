i = input()
x = []
ci = 0
while i != 'end':
    x.append(list(map(int, i.split())))
    i = input()
    ci += 1
cj = len(x[0])
[([print(x[i - 1][j] + x[i][j - 1] + x[i][(j + 1) % cj] + x[(i + 1) % ci][j], end=' ') for j in range(cj)], print()) for i in range(ci)]
