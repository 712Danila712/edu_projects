n = int(input())
i = 0

while i < n:
    if n % i == 0:
        print("NO")
        exit(0)
    i += 1

print("YES")