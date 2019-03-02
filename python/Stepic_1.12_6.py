x = int(input())
n = "программист"
if x % 10 == 0 or x % 10 == 5 or x % 10 == 6 or x % 10 == 7 or x % 10 == 8 or x % 10 == 9:
    print(x, n + "ов")
if x % 10 == 1:
    if x % 100 == 11:
        print(x, n + "ов")
    else:
        print(x, n)
if x % 10 == 2:
    if x % 100 == 12:
        print(x, n + "ов")
    else:
        print(x, n + "а")
if x % 10 == 3:
    if x % 100 == 13:
        print(x, n + "ов")
    else:
        print(x, n + "а")
if x % 10 == 4:
    if x % 100 == 14:
        print(x, n + "ов")
    else:
        print(x, n + "а")






