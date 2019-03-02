x = int(input())
k = 1
while x //(10 ** k) > 0:
    x -= ((x //(10 ** k)) % 10) * (10 ** k)
    k += 2
print(x)
