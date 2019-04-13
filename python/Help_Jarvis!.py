n = int(input())

for i in range(n):
    l = input()
    lst = []

    for k in l:
        lst.append(int(k))
    lst.sort()

    for j in range(len(lst) - 1):
        if lst[j + 1] - lst[j] != 1:
            print("NO")
            break
    else:
        print("YES")