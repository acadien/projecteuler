#!/usr/bin/python

from math import *
import numpy

#Load the matrix
mfil=open("matrix.txt","r")
matrix=[[int(i) for i in line.split(",")] for line in mfil]

N=len(matrix[-1]) #Matrix is size NxN

space=[matrix[i][N-1] for i in range(N)]

for i in range(N-2,-1,-1):
    space[0]+=matrix[0][i]
    for j in range(1,N):
        space[j]=min(space[j-1]+matrix[j][i],space[j]+matrix[j][i])
    for j in range(N-2,-1,-1):
        space[j]=min(space[j],space[j+1]+matrix[j][i])
print min(space)
