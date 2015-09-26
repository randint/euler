##target = 4000000
##fib1, fib2, sum = 1, 2, 0
##
##while fib2 <= target:
##    if fib2 % 2 == 0:
##        sum += fib2
##    fib2 += fib1
##    fib1 = fib2 - fib1
##print sum

##while fib2 <= target:
##    sum += fib2
##    fib1, fib2 = fib1 + 2 * fib2, 2 * fib1 + 3 * fib2
##print sum

def sumFibE(target):
    fib1, fib2, sum = 1, 2, 0
    while fib2 < target:
        sum += fib2
        fib1, fib2 = fib1 + 2 * fib2, 2 * fib1 + 3 * fib2
    return sum

print sumFibE(4000000)
