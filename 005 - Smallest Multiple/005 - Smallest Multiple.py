import array
import math

##1
##2=2
##3=3
##4=2*2
##5=5
##6=2*3
##7=7
##8=2*2*2
##9=3*3
##10=2*5
##
##LCM(1,10)=2*2*2*3*3*5*7=2520

##1
##2=2
##3=3
##4=2*2
##5=5
##6=2*3
##7=7
##8=2*2*2
##9=3*3
##10=2*5
##11=11
##12=2*2*3
##13=13
##14=2*7
##15=3*5
##16=2*2*2*2
##17=17
##18=2*3*3
##19=19
##20=2*2*5
##
##LCM(1,20)=2*2*2*2*3*3*5*7*11*13*17*19=232792560

def factorize(n):
    factors = array.array('i')
    if n % 2 == 0:
        lastFactor = 2
        factors.append(2)
        n = n / 2
        while n % 2 == 0:
            factors.append(2)
            n = n / 2        
    else:
        lastFactor = 1
    factor = 3
    maxFactor = math.sqrt(n)
    while n > 1 and factor <= maxFactor:
        if n % factor == 0:
            lastFactor = factor
            factors.append(factor)
            n = n / factor
            while n % factor == 0:
                factors.append(factor)
                n = n / factor
            maxFactor = math.sqrt(n)
        factor = factor + 2
    if n != 1:
        lastFactor = n
        factors.append(n)
    return factors


def lcm(start, end):
    superset = array.array('i')
    for n in range(start, end + 1):
        subset = factorize(n)
        for i in subset:
            while superset.count(i) < subset.count(i):
                superset.append(i)
    print sorted(superset)
    product = 1
    for factor in superset:
        product *= factor
    return product

def lcm(values):
    superset = array.array('i')
    for n in values:
        subset = factorize(n)
        print str(n) + ": " + str(sorted(subset))
        for i in subset:
            while superset.count(i) < subset.count(i):
                superset.append(i)
    print "LCM: " + str(sorted(superset))
    product = 1
    for factor in superset:
        product *= factor
    return product

print lcm([324,216])
print lcm(range(100,400))
