x = [int(i) for i in input().split()]
n = int(input())
b = []
m = 0
for k in x:
    if k == n:
        print(m, end=" ")
    m += 1
if n not in x:
    print("Отсутствует")
