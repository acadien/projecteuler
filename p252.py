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

#Computes the area of a collection of points
def area(points):
    return 1.0

#Generate a neighbor list
def genNeighbs(points):
    return () #neighbor lists should be sets

#returns False if a polygon is not convex
def is_convex(points): #Check the gift wrapping algorithm
    return False

#Generate all triangles from the neighbor lists
#Remove any triangles that have a point in them

#Save a copy of this list of triangles, and never change it call it all_triangles expecting ~approx 240,000 triangles.

#Start a list of polygons: it should be the subset of all triangles such that each triangle does not share points.

#Find triangles that share 2 common points... join them IF the completed structure is still convex
#keep on adding points to polygons 

#Need to find the area of the largest convex hole in T
T=points()

#Start by 

for i in T:
    pl.scatter(*i)
    print i
pl.show()
