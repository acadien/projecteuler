#!/usr/bin/python

from math import *
from numpy import *
from matplotlib import cm
import pylab as pl
ellipse=lambda x,y:4*x*x+y*y
radius=100

#Given a vector defined by two points, returns the reflected vector off of the ellips
def reflect(start,end):
    x1,y1=start
    x2,y2=end
    theta = atan(-y2/x2/4.)
    rotM = array([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]])
    incoming = array([x2-x1,y2-y1])
    rotated = dot(rotM,incoming)
    rotated[0]*=-1
    outgoing = dot(rotated,rotM)

    m = outgoing[1]/outgoing[0] # slope
    g = y2-m*x2                 # y-intercept
    return m,g

def nextPoint(point,m,g):
    x,y=point
    A=-m*g
    B=sqrt(m*m*g*g-(4+m*m)*(g*g-radius))
    C=4+m*m
    xn1=(A+B)/C
    xn2=(A-B)/C

    if xn1-x < 1E-4:
        xnext = xn2
    else:
        xnext = xn1

    ynext=sqrt(radius-4*xnext*xnext)

    newslope = (ynext-y)/(xnext-x)

    if fabs(newslope - m) > 1E-4:
        ynext *= -1

    return [xnext,ynext]

start=[0,10.1]
end = [1.4,-9.6]

points=[start,end]

for i in range(500):
    m,g = reflect(start,end)
    newend = nextPoint(end,m,g)
    points.append(newend)
    if fabs(newend[0]) <= 0.01 and newend[1]>0:
        print "Success on reflection number",i+1
        break
    start=end
    end=newend

def unpack2rgb(intcol):
    intcol=float(intcol)
    tmp, blue= divmod(intcol, 256)
    tmp, green= divmod(tmp, 256)
    alpha, red= divmod(tmp, 256)
    return alpha, red, green, blue

for i in range(len(points)-1):
    pl.plot(*zip(*points[i:i+2]),c=cm.jet(float(i)/len(points)))
pl.xlim([-8,8])
pl.ylim([-12,12])
pl.show()

