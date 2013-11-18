#!/usr/bin/python
from math import log

vs=list()
for num in range(2,1000):
    value=1
    for p in range(2,30):
        value = pow(num,p)
        if len(str(value))<2: continue
        v=sum(map(int,str(value)))
        if v==num:
            vs.append(value)
svs = sorted(list(set(vs)))

print svs[29]
