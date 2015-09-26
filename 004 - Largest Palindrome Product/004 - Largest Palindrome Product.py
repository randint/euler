import math

# import timeit
# timeit.repeat("f1(x)", "from __main__ import f1", repeat=3, number=100)

# Digits    Greatest
# 1         9 * 1 = 9
# 2         99 * 91 = 9009
# 3         993 * 913 = 906609
# 4         9999 * 9901 = 99000099
# 5         99989 * 99681 = 9966006699
# 6         999999 * 999001 = 999000000999
# 7         9998017 * 9997647 = 99956644665999
# 8         99999999 * 99990001 = 9999000000009999
# 9         
# 10        9999999999 * 9999900001 = 99999000000000099999

# Much slower than using string array methods
def reverse(n):
    reversed = 0
    while n > 0:
        reversed = 10 * reversed + n % 10
        n = n / 10
    return reversed

##def largestPalindromeProduct(factorDigits):
##    largestFound = 0
##    for i in range(int((math.pow(10, factorDigits - 1))), int(math.pow(10, factorDigits))):
##        for j in range(int(math.pow(10, factorDigits -1)), int(math.pow(10, factorDigits))):
##            if str(i * j) == str(i * j)[::-1]:
##                print "%d * %d = %d" % (i, j, i * j)
##                if i * j > largestFound:
##                    largestFound = i * j
##    return largestFound

# Does not repeat any factor pairs => roughly twice as fast   
##def largestPalindromeProduct(factorDigits):
##    largestFound = 0
##    for i in range(int((math.pow(10, factorDigits - 1))), int(math.pow(10, factorDigits))):
##        for j in range(i, int(math.pow(10, factorDigits))):
##            if str(i * j) == str(i * j)[::-1]:
##                print "%d * %d = %d" % (i, j, i * j)
##                if i * j > largestFound:
##                    largestFound = i * j
##    return largestFound

# Try largest factors first and continue downwards
##def largestPalindromeProduct(factorDigits):
##    largestFound = 0
##    for i in reversed(xrange(int((math.pow(10, factorDigits - 1))), int(math.pow(10, factorDigits)))):
##        for j in reversed(xrange(int(math.pow(10, factorDigits - 1)), i + 1)):
##            if str(i * j) == str(i * j)[::-1]:
##                print "%d * %d = %d" % (i, j, i * j)
##                if i * j > largestFound:
##                    largestFound = i * j
##    return largestFound

# Skip smaller factor pairs once a palindrome product is found for a given factor
##def largestPalindromeProduct(factorDigits):
##    largestFound = 0
##    for i in reversed(xrange(int((math.pow(10, factorDigits - 1))), int(math.pow(10, factorDigits)))):
##        for j in reversed(xrange(int(math.pow(10, factorDigits - 1)), i + 1)):
##            if str(i * j) == str(i * j)[::-1]:
##                print "%d * %d = %d" % (i, j, i * j)
##                if i * j > largestFound:
##                    largestFound = i * j
##                break
##    return largestFound

# End once remaining factor pairs cannot produce greater products
##def largestPalindromeProduct(factorDigits):
##    largestFound = 0
##    for i in reversed(xrange(int((math.pow(10, factorDigits - 1))), int(math.pow(10, factorDigits)))):
##        if largestFound >= i * i:
##            break
##        for j in reversed(xrange(int(math.pow(10, factorDigits - 1)), i + 1)):
##            if str(i * j) == str(i * j)[::-1]:
##                print "%d * %d = %d" % (i, j, i * j)
##                if i * j > largestFound:
##                    largestFound = i * j
##                break
##    return largestFound

# More aggressively ends once remaining factor pairs cannot produce greater products
# Each product found is guaranteed to be greater than the last
# Increasing optimization as value of last product found increases
##def largestPalindromeProduct(factorDigits):
##    largestFound = 0
##    for i in reversed(xrange(int((math.pow(10, factorDigits - 1))), int(math.pow(10, factorDigits)))):
##        if largestFound >= i * i:
##            break
##        for j in reversed(xrange(int(math.pow(10, factorDigits - 1)), i + 1)):
##            if largestFound >= i * j:
##                break
##            if str(i * j) == str(i * j)[::-1]:
##                print "%d * %d = %d" % (i, j, i * j)
##                if i * j > largestFound:
##                    largestFound = i * j
##                break
##    return largestFound


##def largestPalindromeProduct(factorDigits):
##    largestFound = 1
##    for i in reversed(xrange(int((math.pow(10, factorDigits - 1))), int(math.pow(10, factorDigits)))):
##        if largestFound >= i * i:
##            break
##        for j in reversed(xrange(max(int(math.pow(10, factorDigits - 1)), largestFound / i), i + 1)):
##            if str(i * j) == str(i * j)[::-1]:
##                print "%d * %d = %d" % (i, j, i * j)
##                largestFound = i * j
##                break
##    return largestFound

# Improved try largest factors first
##def largestPalindromeProduct(factorDigits):
##    largestFound = 0
##    for i in reversed(xrange(int((math.pow(10, factorDigits - 1))), int(math.pow(10, factorDigits)))):
##        if largestFound >= i * (math.pow(10, factorDigits) - 1):
##            break
##        for j in reversed(xrange(i, int(math.pow(10, factorDigits)))):
##            if largestFound >= i * j:
##                break
##            if str(i * j) == str(i * j)[::-1]:
##                print "%d * %d = %d" % (i, j, i * j)
##                if i * j > largestFound:
##                    largestFound = i * j
##                break
##    return largestFound

# Try range further narrowed so that tested factor pairs can strictly produce a greater product
# Marginally faster for 7 factorDigits than alternate
##def largestPalindromeProduct(factorDigits):
##    largestFound = 0
##    for i in reversed(xrange(int((math.pow(10, factorDigits - 1))), int(math.pow(10, factorDigits)))):
##        if largestFound >= i * (math.pow(10, factorDigits) - 1):
##            break
##        for j in reversed(xrange(max(i, int(math.ceil(largestFound / float(i)))), int(math.pow(10, factorDigits)))):
##            if largestFound >= i * j:
##                break
##            if str(i * j) == str(i * j)[::-1]:
##                print "%d * %d = %d" % (i, j, i * j)
##                if i * j > largestFound:
##                    largestFound = i * j
##                break
##    return largestFound

# Unnecessary checks removed
##def largestPalindromeProduct(factorDigits):
##    largestFound = 0
##    for i in reversed(xrange(int((math.pow(10, factorDigits - 1))), int(math.pow(10, factorDigits)))):
##        if largestFound >= i * (math.pow(10, factorDigits) - 1):
##            break
##        for j in reversed(xrange(max(i, int(math.ceil(largestFound / float(i)))), int(math.pow(10, factorDigits)))):
##            if str(i * j) == str(i * j)[::-1]:
##                print "%d * %d = %d" % (i, j, i * j)
##                largestFound = i * j
##                break
##    return largestFound

# Only check factor pairs where at least one factor is a multiple of 11
##def largestPalindromeProduct(factorDigits):
##    largestFound = 0
##    if factorDigits == 1:
##        return 9
##    for i in reversed(xrange(int((math.pow(10, factorDigits - 1))), int(math.pow(10, factorDigits)))):
##        if largestFound >= i * (math.pow(10, factorDigits) - 1):
##            break
##        if i % 11 == 0:
##            j = int(math.pow(10, factorDigits))
##            dj = 1
##        else:
##            j = int(math.pow(10, factorDigits)) / 11 * 11
##            dj = 11
##        while j > i and j > largestFound / i:
##            if str(i * j) == str(i * j)[::-1]:
##                print "%d * %d = %d" % (i, j, i * j)
##                largestFound = i * j
##                break
##            j = j - dj
##    return largestFound

# For loop version, slightly faster
def largestPalindromeProduct(factorDigits):
    largestFound = 0
    if factorDigits == 1:
        return 9
    for i in reversed(xrange(int((math.pow(10, factorDigits - 1))), int(math.pow(10, factorDigits)))):
        if largestFound >= i * (math.pow(10, factorDigits) - 1):
            break
        if i % 11 == 0:
            j1 = max(i, int(math.ceil(largestFound / float(i))))
            j2 = int(math.pow(10, factorDigits))
            dj = 1
        else:
            j1 = int(math.ceil(max(i, math.ceil(largestFound / float(i))) / float(11)) * 11)
            j2 = int(math.pow(10, factorDigits)) / 11 * 11
            dj = 11
        for j in reversed(xrange(j1, j2 + 1, dj)):
            if str(i * j) == str(i * j)[::-1]:
                print "%d * %d = %d" % (i, j, i * j)
                largestFound = i * j
                break
    return largestFound

##for x in range(100):
    print largestPalindromeProduct(x)

##for i in reversed(xrange(10, 100/11*11+1)):
##    for j in reversed(xrange(i, 11)):
##        print i, j, i * j

##for i in reversed(xrange(int(math.ceil(10 / float(11))) * 11, 100, 11)):
##    print i
