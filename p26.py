#!/usr/bin/python
from decimal import *

def repeats(numbs):
    if len(numbs)<51:
        return 0

    reps=numbs[2:12]
    #numbs=numbs[12:]
    strt=numbs.find(reps,12)
    if strt < 0: return 0
    if strt < len(numbs)/2:
        #print numbs[2:strt+1],numbs[2:strt*2]
        return strt
    return 0

getcontext().prec = 2000

maxre=0
maxd=1
for d in range(200,1000):
    re=repeats(str(Decimal(1)/Decimal(d)))
    
    if re>maxre:
        maxre=re
        maxd=d
        print maxd,maxre#,Decimal(1)/Decimal(d)

