N = int(input())
a = list(map(int, input().split()))
lst = [0 for i in range(1001)]

Q = int(input())

for i in a:
    lst[i] += 1

for i in range(Q):
    q = lst[int(input())]
    if q == 0:
        print("NOT PRESENT")
    else:
        print(q)
