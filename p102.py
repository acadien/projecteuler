#!/usr/bin/python

from math import *
from numpy import *

triangles=[array(map(float,line.split(","))) for line in open("triangles.txt","r")]

origin=array([0.,0.])

def containsOrigin(triangle):
    triangle.shape=[3,2]
    v0=triangle[2]-triangle[0]
    v1=triangle[1]-triangle[0]
    v2=origin-triangle[0]

    dot00 = dot(v0, v0)
    dot01 = dot(v0, v1)
    dot02 = dot(v0, v2)
    dot11 = dot(v1, v1)
    dot12 = dot(v1, v2)

    invDenom = 1 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * invDenom
    v = (dot00 * dot12 - dot01 * dot02) * invDenom


    return (u >= 0) and (v >= 0) and (u + v < 1)

print sum([1 for i in range(len(triangles)) if containsOrigin(triangles[i])])
    
    
