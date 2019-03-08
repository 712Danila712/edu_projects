x = [int(i) for i in input().split()]
m = 0
for n in x:
    if n > m:
        m = n
print(m)
    