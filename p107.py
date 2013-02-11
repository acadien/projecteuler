#!/usr/bin/python

from numpy import *

#Implement prims algorithm to calculate a minimum spanning tree.

#Read in the graph
def conv(x):
    try:
        return int(x)
    except ValueError:
        return 0
graph = array([map(conv,line.split(",")) for line in open("network.txt","r").readlines()])
n=graph.shape[0]

total=sum([sum([graph[i,j] for j in range(i,n)]) for i in range(n)])

def grab_edges(vert,verts,graph):
    return [(vert,j,graph[vert,j]) for j in range(n) if graph[vert,j]!=0 and j not in verts]

mst=zeros([n,n])

#Set a Starting point
verts=[0]
edges=grab_edges(0,verts,graph)
tot=0
while len(verts)<n:
    edges = sorted(edges,key=lambda x:x[2])

    mvert=[-1,-1]
    mval=1E10
    while True:
        mvert[0],mvert[1],mval=list(edges.pop(0))
        if mvert[1] not in verts:
            break

    #Add the new vertex
    verts.append(mvert[1])

    #Add new edges to edge list
    edges += grab_edges(mvert[1],verts,graph)

    #Add edge to mst
    mst[mvert[0],mvert[1]]=mval
    tot+=mval

print total-tot
