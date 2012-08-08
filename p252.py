#!/usr/bin/python

from math import *
from scipy import array,zeros
import pylab as pl

def points():
    S=range(1001)
    S[0]=290797
    T=zeros(1000)
    for i in range(1,1001):
        S[i]=(S[i-1]**2)%50515093
        T[i-1]=S[i]%2000-1000
    print T[0:3]
    return T.reshape([500,2])


#Need to find the area of the largest convex hole in T
T=points()

for i in T:
    pl.scatter(*i)
    print i
pl.show()
