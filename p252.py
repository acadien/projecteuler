#!/usr/bin/python

from math import *
from scipy import array,zeros
import pylab as pl

def points():
    npoints=500
    S=range(npoints*2+1)
    S[0]=290797
    T=zeros(npoints*2)
    for i in range(1,npoints*2+1):
        S[i]=(S[i-1]**2)%50515093
        T[i-1]=S[i]%2000-1000
    return T.reshape([npoints,2])

points=points()

r=250
r2=r**2
counts=list()
density=list()
for i in range(-1000+r,1001-r,50):
    for j in range(-1000+r,1001-r,50):
        counts.append(0)
        density.append([i,j])
        for x,y in points:
            if ((x-i)**2+(y-j)**2)<r2:
                counts[-1]+=1
            
pl.scatter(*points.T.tolist())
xs,ys=zip(*density)
pl.scatter(xs,ys,counts)


pl.show()
