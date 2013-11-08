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

            lastdig=set(str(f%1000000000))
            if len(lastdig)!=9 or "0" in lastdig:
                continue
            ndig=int(log10(f))
            frstdig=set(str(f/10**(ndig-8)))

            #Test
            #if len(frstdig)==9:
            #    print "first",k,frstdig,lastdig#,len(sfib)
            #if len(lastdig)==9:
            #    print "last",k,frstdig,lastdig#,len(sfib)

            #Final solution.
            if len(frstdig)==9 and "0" not in frstdig:
                print "win",k,frstdig,lastdig#,len(sfib)
                break

        if k>1000000: 
            break

pangeafib(0)

