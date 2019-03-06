L = int(input())
N = int(input())
b = []
m = 0
for i in range(N):
     b += [int(k) for k in input().split()]
while len(b) != 0:
    if b[m] == L and b[m + 1] == L:
        print("ACCEPTED")
    if b[m] > L and b[m + 1] > L:
        if b[m] == b[m + 1]:
            print("ACCEPTED")
        else:
            print("CROP IT")
    if b[m] < L or b[m + 1] < L:
        print("UPLOAD ANOTHER")
    del b[m]
    del b[m]
     
    
    
    
