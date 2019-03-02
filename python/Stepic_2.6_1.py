x = int(input())
s = x
k = x ** 2
while s != 0:
    x = int(input())
    k += x ** 2 
    s += x
print(k)
