n = int(input())
lst = []
l = [int(input()) for j in range(n)]
for i in l:
    while i > 0:
        lst.append(i % 10)
        i //= 10
    lst.sort()
    for k in range(len(lst)):
        if k == len(lst) - 1:
            if lst[-1] - lst[-2] > 1:
                print("NO")
                break
            else:
                print("YES")
        else:
            if lst[k + 1] - lst[k] > 1:
                print("NO")
                break
            else:
                print("YES")
        
            
        
    lst = []

