#!/usr/bin/python
from math import *

tot=0

fct={0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}

for i in range(3,1E6):
    ii=str(i)
    loctot=0
    for dig in ii:
        loctot+=fct[int(dig)]
    if loctot==i:
        tot+=loctot
        print loctot
print tot

