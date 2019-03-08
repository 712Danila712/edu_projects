L = int(input())
N = int(input())
b = []
m = 0
for i in range(N):
    temp = list(map(int, input().split()))
    if temp[0] < L or temp[1] < L:
        print("UPLOAD ANOTHER")
    elif temp[0] == temp[1]:
        print("ACCEPTED")
    else:
        print("CROP IT")
    
