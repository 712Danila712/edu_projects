s = [int(i) for i in input().split()]
a = 0
for k in range(s[0],s[1] + 1):
    if k % s[2] == 0:
        a += 1
print(a)
