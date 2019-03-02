x = int(input())
n = (x // 1000) % 10
m = (x // 10) % 10
print(x - n * 1000 - m * 10 )
