import math


def isPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


n = int(input())

for i in range (2, n):
    if isPrime(i):
        print(i, end=' ')