#!/usr/bin/python
from math import *
#mine
from PEutil import *

mxnum=50e6
mxroot=sqrt(mxnum)

allprimes=primesfrom2to(mxroot+5)

allprimes2=[i*i for i in allprimes]
allprimes3=[i*i*i for i in allprimes]
allprimes4=[i*i*i*i for i in allprimes]

#Remove all primepowers greater than mxnum to avoid overflow errors

def chop_series(series,mx):
    for i,val in enumerate(series):
        if val>mx:
            break
    return series[:i+1]

allprimes2=chop_series(allprimes2,mxnum)
allprimes3=chop_series(allprimes3,mxnum)
allprimes4=chop_series(allprimes4,mxnum)

vals=list()
for i in allprimes4:
    for j in allprimes3:
        for k in allprimes2:
            s=i+j+k
            if s<mxnum:
                vals.append(s)
vals=list(set(vals))
print len(vals)

