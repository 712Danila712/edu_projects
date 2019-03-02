a = int(input())
b = int(input())
h = int(input())
if a > b:
    print("Ошибка")
else:
    if h < a:
        print("Недосып")
    elif h > b:
        print("Пересып")
    else:
        print("Это нормально")
