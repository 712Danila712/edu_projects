x = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(x[1]):
    f = list(map(int, input().split()))
    if f[0] == 1:
        b[f[1] - 1] = (b[f[1] - 1] + 1) % 2
    else:
        if b[f[2] - 1] == 1:
            print("ODD")
        else:
            print("EVEN")
