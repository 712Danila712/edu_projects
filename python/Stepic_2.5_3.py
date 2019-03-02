le = [int(i) for i in input().split()]
le.sort()
m = []
for i in range(len(le)):
    if i > 0:
        if le[i] == le[i - 1]:
            if le[i] not in m:
                m += [le[i]]
for i in m:
    print(i, end=" ")
