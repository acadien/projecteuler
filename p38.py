#!/usr/bin/python

pand=set(['1','2','3','4','5','6','7','8','9'])

def ispand(numstr):
    numstr=[i for i in numstr]
    setstr=set(numstr)
    if len(numstr)!=len(setstr):
        return False
    if pand!=setstr:
        return False
    return True

def trydig(n):
    ss=str(n)
    if len(ss)<4:
        mxj=9/len(ss)
    else:
        mxj=2
    cont=""
    val=''.join([str(n*j) for j in range(1,mxj+1)])

    if ispand(val):
        return val
    return -1

pandas=list()
for i in range(1,10):
    a=trydig(i)
    if a>-1:
        pandas.append(a)

for i in range(100,1000):
    a=trydig(i)
    if a>-1:
        pandas.append(a)

for i in range(5123,10000):
    a=trydig(i)
    if a>-1:
        pandas.append(a)



print max(pandas)
