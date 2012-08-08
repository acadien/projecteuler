#!/usr/bin/python
import sys
from math import *

def pangeafib():
    digs=map(str,range(1,10))
    print digs
    n1=0
    n2=1
    k=1
    while True:
        f=n1+n2
        n1=n2
        n2=f
        k+=1
        if k==150: 
            print f
            sfib=str(f)
            frstdig=sorted(sfib[:9])
            lastdig=sorted(sfib[-9:])
            print frstdig
            print lastdig
            break
        sfib=str(f)
        frstdig=sorted(sfib[:9])
        lastdig=sorted(sfib[-9:])
        if frstdig==digs:
            print "first",k,frstdig,lastdig,len(sfib)
            break
        elif lastdig==digs:
            print "last",k,frstdig,lastdig,len(sfib)
        if k>1000: break

pangeafib()

