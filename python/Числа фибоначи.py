n = 10
a = -1
c = 0
for i in range(n):
    print(abs(a + c))
    b = a
    a = c
    c = b + a
    
