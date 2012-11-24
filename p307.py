#!/usr/bin/python
from math import *
from random import *
import sys

nd=int(sys.argv[1]) #number of defects
nc=int(sys.argv[2]) #number of chips
N=int(sys.argv[3]) #number of iterations

chips=range(nc)
defects=range(nd)
seed(121)

def countTriplicates(duplist):
    uniq=set(i for i in duplist)
    return sum([1 for item in sorted(uniq) if duplist.count(item)>2])

tot=0.0
for i in range(N):
    for j in range(nd):
        defects[j]=choice(chips)
    temp=countTriplicates(defects)
    tot+=float(temp)/float(nc)
    if i%1000==0:
        print "run:%d, #defct:%d, c3d:%g, avg:%12.12g" % (i,temp,float(temp)/float(nc),tot/float(i+1))


tot/=float(N)
print "Average probabiility a chip has >2 defects (with 12 digits):\n %12.12g" % tot

    

