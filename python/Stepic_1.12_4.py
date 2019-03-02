f = input()
if f == "прямоугольник":
    a = float(input())
    b = float(input())
    print(a * b)
elif f == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif f == "круг":
    pi = 3.14
    r = float(input())
    print(pi * r ** 2)
else:
    print("введена неверная фигура!")
    
