import math

def sumNaturalNumbers(n):
    return n * (n + 1) / 2

def sumNaturalNumbersSquares(n):
    sum = 0
    for i in range(n + 1):
        sum += i * i
    return sum

n = 100
print math.pow(sumNaturalNumbers(n), 2) - sumNaturalNumbersSquares(n)
