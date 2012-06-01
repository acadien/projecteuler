#!/usr/bin/python

from math import *
import numpy

#Load the matrix
mfil=open("testmat.txt","r")
matrix=[[int(i) for i in line.split(",")] for line in mfil]

N=len(matrix[-1]) #Matrix is size NxN

def minpathUDR(matrix,N,i,j):
    last="N"
    while j<N-1:
        a=1E10
        b=1E10
        c=1E10
        if last=="U":
            if i==0:
                b=matrix[i][j+1] #move right
            else:
                b=matrix[i][j+1] #move right
                c=matrix[i+1][j] #move down
                matrix[i][j]+=mn

            
    return matrix[0][0]
