import array
import math

# A prime number is an integer that has exactly 2 integer divisors: 1 and itself
# The first ten prime numbers are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 27
# Other than 2, every prime number is odd since otherwise it would be divisible by 2
# Other than 5, no prime number ends in 5 since otherwise it would be divisible by 5
# After 5, every prime number ends in either 1, 3, 7, or 9
# Every integer greater than 1 has exactly one unique prime factorization
# The greatest factor of an integer, other than itself, is at most its square root

# Some of these facts can be used to achieve minor to major optimizations
# Minor (linear) optimizations: Checking only odd integers after 2 => up to 2 times faster
# Major optimizations: Checking only up to square root => up to more than sqrt(n) times faster
# Major optimizations yield huge efficiency gains as n increases
# Ex: For n=982451653 (which is prime), stopping after sqrt(n) => 31344 times faster

# Initial setup
number = 500000001
factors = array.array('i')

# Simple algorithm tests all integers
# [2, 3, 4, 5, ..., n)
##def isPrime(n):
##    if n < 2:
##        return False
##    factor = 2
##    while factor < n:
##        if n % factor == 0:
##            return False
##        factor = factor + 1
##    return True

# Significantly optimized algorithm tests only up to square root of n
# [2, 3, 4, 5, ..., sqrt(n)]
##def isPrime(n):
##    if n < 2:
##        return False
##    factor = 2
##    while factor <= math.sqrt(n):
##        if n % factor == 0:
##            return False
##        factor = factor + 1
##    return True

# Additionally handles 2 separately and tests only odd integers afterwards
# [2k, 3, 5, 7, ..., sqrt(n)]
##def isPrime(n):
##    if n < 2:
##        return False
##    if n == 2:
##        return True
##    if n % 2 == 0:
##        return False
##    factor = 3
##    while factor <= math.sqrt(n):
##        if n % factor == 0:
##            return False
##        factor = factor + 2
##    return True

# Handles divisibility by 2 or 3 separately and then tests only integers 6k-1, 6k+1 afterwards
# [2k, 3k, 5, 7, 11, 13, ..., sqrt(n)]
def isPrime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    k = 6
    while k - 1 <= math.sqrt(n):
        if n % (k - 1) == 0 or n % (k + 1) == 0:
            return False
        k = k + 6
    return True

# Tests isPrime to print first primes
##n = 0
##found = 0
##lastPrime = 0
##sumOfDifferences = 0
##averageDifference = 0
##
##while found < 5000:
##    if isPrime(n):
##        found = found + 1
##        if found > 1:
##            sumOfDifferences += n - lastPrime
##            averageDifference = sumOfDifferences / (found - 1.0)
##            print n, averageDifference
##        else:
##            print n
##        lastPrime = n
##    n = n + 1

##while n <= 3:
##    if isPrime(n):
##        # print n
##        found = found + 1
##    n = n + 1
##n = 6
##while found <= 100000:
##    if isPrime(n - 1):
##        # print n
##        found = found + 1
##    if isPrime(n + 1):
##        # print n
##        found = found + 1
##    n = n + 6
##while found <= 101000:
##    if isPrime(n - 1):
##        print n
##        found = found + 1
##    if isPrime(n + 1):
##        print n
##        found = found + 1
##    n = n + 6
    
##factor = 2
##while factor <= n:
##    if n % factor == 0:
##        print "%d / %d = %d" % (n, factor, (float(n) / factor))
##        largestPrime = factor
##        n = n / factor # divide the n
##        # below line is unnecessary since all factors will be greater than or equal to last one found
##        factor = 2 # reset index (check for another prime factor starting with 2 again)
##    else:
##        factor = factor + 1

def factorize(n):
    if n % 2 == 0:
        print "%d / %d = %d" % (n, 2, n / 2)
        lastFactor = 2
        # factors.append(2)
        n = n / 2
        while n % 2 == 0:
            print "%d / %d = %d" % (n, 2, n / 2)
            # factors.append(2)
            n = n / 2        
    else:
        lastFactor = 1
    factor = 3
    maxFactor = math.sqrt(n)
    while n > 1 and factor <= maxFactor:
        if n % factor == 0:
            print "%d / %d = %d" % (n, factor, n / factor)
            lastFactor = factor
            # factors.append(factor)
            n = n / factor
            while n % factor == 0:
                print "%d / %d = %d" % (n, factor, n / factor)
                # factors.append(factor)
                n = n / factor
            maxFactor = math.sqrt(n)
        factor = factor + 2
    if n != 1:
        lastFactor = n
        # factors.append(n)
    return lastFactor

##print factorize(500000007)

x = 1000000000000000000000000000000000000000003
while not isPrime(x):
    print str(factorize(x)) + '\n'
    x += 1
print x



# Error-checking script confirms whether found factors multiply to original number
##check = 1
##factorization = ""
##for x in factors:
##    check *= x
##    print x
##    if len(factorization) == 0:
##        factorization += "%d" % x
##    else:
##        factorization += " * %d" % x
##factorization += " = %d" % check
##print factorization
##print check == number
