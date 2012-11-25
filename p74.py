#!/usr/bin/python
from math import *
from itertools import permutations

def factChainStep(n):
    return sum(map(lambda x:factorial(int(x)),str(n)))

maxval=1000000
MagicNumber=60
found=[]
notfound=[]
cnt=0
for i in range(1,maxval):
#    if i in found: continue
    if i>223479 and i%100==0:
        print i
    vals=[i]
    bad=False
    for j in range(MagicNumber):
        vals.append(factChainStep(vals[-1]))
        if j<MagicNumber-1 and vals[-1] in vals[:-1]:
            bad=True
            break
    if bad: continue
        
    if vals.count(vals[-1])==2:
        cnt+=1
        print i,cnt,vals

#found+=[int("".join(j)) for j in permutations(str(i))]
    
#print found
#print len(found)
print cnt
