N = int(input())
a = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
    q = int(input)
    if q not in a:
        print("NOT PRESENT")
    else:
        print(a.count(q))