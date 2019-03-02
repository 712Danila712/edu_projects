x = int(input())
h = int(input())
m = int(input())

n = h * 60 + m + x

print(n // 60)
print(n % 60)
