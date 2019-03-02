x = [int(i) for i in input().split()]
b = []
for k in range(len(x) - 1):
    b.append(x[k - 1] + x[k + 1])
b.append(x[len(x) - 2] + x[0])
for j in range(len(x)):
    b[j] = str(b[j])
s = b[0] + " "
n = 1
for m in range(len(x) - 1):
        s += b[n] + " "
        n += 1
if len(x) == 1:
    s = x[0]
print(s)
