#!/usr/bin/python

from math import *

#generate a,c,d from perfect squares
#generate b,e,f from algebraic relationships
#test x,y,z for solution
N=100000
for a in range(4,N):
    a2=a*a

    for c in range(3,a):
        c2=c*c

        f2=a2-c2        
        if f2<=0: continue
        f=sqrt(f2)
        if int(f)!=f: continue
        
        start=2
        if c%2==1:
            start=1
        for d in range(start,c,2):
            d2=d*d

            e2=a2-d2
            if e2<=0: continue
            e=sqrt(e2)
            if int(e)!=e: continue

            b2=c2-e2
            if b2<=0: continue
            b=sqrt(b2)
            if int(b)!=b: continue
            
            x=(d2+c2)/2
            y=(e2+f2)/2
            z=(c2-d2)/2
            print x,y,z,x+y+z
            if x>y>z>0:
                print a,b,c,d,e,f,x+y+z,"success"
                exit(0)
