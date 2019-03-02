s = input()
k = 1
x = 1
n = s[x:x+1]
for i in s:
    if i in n:
        k += 1
    else:
        print(i, end='')
        print(k, end='')
        k = 1
    x += 1
    n = s[x:x+1]
