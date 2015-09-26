target = 99999999

# Linear time
##def sumDivisibleBy(n):
##    sum = 0
##    current = 1
##    while current <= target:
##        if current % n == 0:
##            sum += current
##        current += 1
##    return sum

# Improved linear time proportional to n, no need for division
##def sumDivisibleBy(n):
##    sum = 0
##    current = n
##    while current <= target:
##        sum += current
##        current += n        
##    return sum

# Constant time
 def sumDivisibleBy(n):
    p = target // n # floor division (rounds down final answer)
    sum = n * (p * (p + 1)) / 2 # n * (1 + 2 + 3 + ... + p)
    return sum
    
print sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15)
