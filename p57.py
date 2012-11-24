#!/usr/bin/python
from math import *

#The idea:
#calculate all numerators of root 2 expansions
#calculate all denominators of root 2 expansions
#Count all len(numer)>len(denom)
numers=[1,3]
denoms=[1,2]
for i in range(2,1001):
    numers.append(numers[i-1]*2+numers[i-2])
    denoms.append(denoms[i-1]*2+denoms[i-2])

numers=[str(numers[i-1]) for i in range(1,1001)]
denoms=[str(denoms[i-1]) for i in range(1,1001)]
    
print sum([1 for i in range(len(numers)) if len(numers[i])>len(denoms[i])])
