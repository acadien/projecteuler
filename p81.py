#!/usr/bin/python

from math import *
import numpy

#Load the matrix
mfil=open("matrix.txt","r")
matrix=[[int(i) for i in line.split(",")] for line in mfil]

N=len(matrix[-1])-1 #Matrix is size NxN

for i in range(N,-1,-1):
    for j in range(N,-1,-1):
        if i==N and j==N: continue
        if i==N: mn = matrix[i][j+1]
        elif j==N: mn = matrix[i+1][j]
        else: mn = min(matrix[i+1][j],matrix[i][j+1])
        matrix[i][j]+=mn

print matrix[0][0]
