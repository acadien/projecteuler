#!/usr/bin/python
import sys
from math import *
from repr import repr

def pangeafib(start):
    digs=map(str,range(1,10))
    n1=0
    n2=1
    k=1
    while True:
        f=n1+n2
        n1=n2
        n2=f
        k+=1
        #sfib=str(f)

        if k%1000==0:
            print k#,len(sfib)

        if k>start:

            ndig=int(log10(f))
            frstdig=sorted(str(f/10**(ndig-8)))
            lastdig=sorted(str(f%int(1E9)))

        #Test
        #if frstdig==digs:
        #    print "first",k,frstdig,lastdig#,len(sfib)
        #if lastdig==digs:
        #    print "last",k,frstdig,lastdig#,len(sfib)

        #Final solution.
            if frstdig==digs and lastdig==digs:
                print "win",k,frstdig,lastdig#,len(sfib)
                break

        if k>1000000: 
            break

pangeafib(250000)

