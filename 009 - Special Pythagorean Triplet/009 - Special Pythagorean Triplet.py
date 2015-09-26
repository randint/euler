import math

##Find the Pythagorean triplet (a, b, c) where a + b + c = 1000

##Triplet     2mn     m^2-n^2         m^2+n^2
##3-4-5       24      7=16-9          25=16+9
##6-8-10      96      28=64-36        100=64+36
##5-12-13     120     119=144-25      169=144+25
##9-12-15     216     63=144-81       225=144+81
##8-15-17     240     161=225-64      289=225+64
##12-16-20    384     112=256-144     400=256+144
##7-24-25     336     527=576-49      625=576+49

# n < m < c
# m + n > c
# m + n + c = 1000
# c: [335 , 499]
# m + n: [501, 665]
# 2mn is always a multiple of 24, so mn is always a multiple of 12
# At least one of m or n is even



def findHypotenuse(a, b):
    return int(math.sqrt(math.pow(a, 2) + math.pow(b, 2)))

def analyzeTriplet(a, b):
    c = int(math.sqrt(math.pow(a, 2) + math.pow(b, 2)))
    print a, b, c
    print '2mn = %d' % (2 * a * b)
    print 'm^2-n^2 = %d' % (math.pow(b, 2) - math.pow(a, 2))
    print 'm^2+n^2 = %d\n' % (math.pow(b, 2) + math.pow(a, 2))
    
##testList = ((3,4),(6,8),(5,12),(9,12),(8,15),(12,16),(7,24))
##for pair in testList:
##    analyzeTriplet(pair[0], pair[1])

##print testList

sumOfSides = 1000
cMin = sumOfSides / 2 + 1
nMax = math.ceil((sumOfSides - cMin) / 2) - 1


for n in range(3, nMax):
    if n % 2 == 1:
        step = 2
    else:
        step = 1
    for m in range(sumOfSides, nMax + 1):
        if 
