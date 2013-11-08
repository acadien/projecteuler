#!/usr/bin/python

from math import *
import numpy

#Hooray no more dynamic programming, lets use a path finding algo A*

#Load the matrix
mfil=open("matrix.txt","r")
matrix=[[int(i) for i in line.split(",")] for line in mfil]
N=len(matrix[-1]) #Matrix is size NxN

#Heuristic cost estimator from any location to the goal
mincost=min(map(min,matrix))
def costEstimate(spot,goal):
    dist= goal[0]-spot[0] + goal[1]-spot[1]
    return dist*mincost

#Who are the current spots neighboring nodes?
def neighbors(spot):
    neighbs=list()
    if spot[0]>0:
        neighbs.append((spot[0]-1,spot[1]))
    if spot[1]>0:
        neighbs.append((spot[0],spot[1]-1))
    if spot[0]<N-1:
        neighbs.append((spot[0]+1,spot[1]))
    if spot[1]<N-1:
        neighbs.append((spot[0],spot[1]+1))
    return neighbs

#Given a path, what is its cost to traverse
def reconstruct(start,path,matrix):
    total=matrix[start[0]][start[1]]
    current=start
    while current!=(0,0):
        current=path.pop(current)
        total+=matrix[current[0]][current[1]]
    return total


#Main
start=(0,0)
goal = (N-1,N-1)
doneQ =list() #closed set
nodeQ = [start]#open set
path = {} #came_from
gScore = {start:0} #cost from start
fScore = {start:costEstimate(start,goal)}
 
while len(nodeQ)>0:
    current = min(fScore.items(),key=lambda x:x[1])[0]
    del fScore[current]
    print current,goal
    nodeQ.remove(current)
    doneQ.append(current)
    
    for neighb in neighbors(current):
        if neighb in doneQ: continue

        if current == goal:
            print "score:",reconstruct(goal,path,matrix)
            exit(0)

        gScoreTrial = gScore[current] + matrix[neighb[0]][neighb[1]]
        if neighb not in nodeQ or gScoreTrial <= gScore[neighb]:
            path[neighb] = current
            gScore[neighb] = gScoreTrial
            fScore[neighb] = gScoreTrial + costEstimate(neighb,goal)
            if neighb not in nodeQ:
                nodeQ.append(neighb)
if current == goal:
    print "score:",reconstruct(goal,path,matrix)
    exit(0)
