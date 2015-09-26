import math

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    factor = 3
    while factor <= math.sqrt(n):
        if n % factor == 0:
            return False
        factor = factor + 2
    return True

def findNthPrime(n):
    found = 0
    lastFound = 0
    i = 2
    while found < n and i <= 3:
        if isPrime(i):
            lastFound = i
            found = found + 1
        i = i + 1
    i = 6
    while found < n:
        if isPrime(i - 1):
            lastFound = i - 1
            found = found + 1
        if found < n and isPrime(i + 1):
            lastFound = i + 1
            found = found + 1
        i = i + 6
    print found
    return lastFound

print findNthPrime(10001)
