#!/usr/bin/python
from math import *
from numpy import *
import pylab as pl


right,up,left,down = (0,1),(1,0),(0,-1),(-1,0)
#rotate clockwise
rcw={right : array(down), down: array(left), left : array(up), up : array(right)} 
#rotate counter clockwise
rccw={right : array(up), up: array(left), left : array(down), down : array(right)}

n=1000

dirn=array([0,1])  #what direction is the ant facing
curr=array([n/2,n/2])       #where is the ant

grid=zeros([n,n])
upBound=array([n,n])
lowBound=array([0,0])
"""
steps=11000
timeseries=[0]
for i in range(steps):
    r,c=curr
    if grid[r,c] == 0: #on a white space
        grid[r,c] = 1
        dirn = rcw[tuple(dirn)]
    else:  #on a black space
        grid[r,c] = 0
        dirn = rccw[tuple(dirn)]
        
    curr += dirn
    if (curr >= upBound).any() or (curr < lowBound).any():
        print curr, "is out of bounds! Stopping."

        break
    s=grid.sum()
    timeseries.append(s)
"""

#Used the above code to generate the series, realized it was periodic
#calculate the slope of the time series after it becomes periodic and 
#extrapolate out the solution at 10**18 steps.

start=10353
end=10457
bstart=765
brun=104
brise=12
bslope=brise/brun
dist=int(10**18)-start

bloop=map(int,"0.  -1.  -2.  -3.  -4.  -3.  -4.  -3.  -2.  -1.   0.  -1.   0.  -1.  -2.  -1.   0.  -1.  -2.  -3.  -4.  -3.  -2.  -3.  -4.  -3.  -2.  -1.   0.  -1.  -2.  -1.   0.  -1.   0.  -1.  -2.  -1.  -2.  -3.  -2.  -3.  -2.  -3.  -4.  -3.  -2.  -1.   0.  -1.  -2.  -1.  -2.  -3.  -2.  -1.   0.   1.   0.  -1.   0.   1.   2.   3.   2.   1.   2.   1.   2.   3.   4.   5.   4.   5.   4.   3.   2.   1.   2.   3.   4.   5.   4.   5.   6.   5.   6.   7.   8.   9.   8.   7.   6.   5.   6.   5.   6.   7.   8.   9.   8.   9.  10.  11.  12".split("."))

nsteps=int(dist/brun)
print bstart+nsteps*12+bloop[dist-nsteps*brun]

