#!/usr/bin/python
from math import *

x=open("triangle.txt","r")

class Node:
    def __init__(self,val,cr,cl,dist=0):
        self.val=val
        self.r=cr
        self.l=cl
        self.dist=dist

def nextr(tree,i):
    right=tree[i].r
    return (right,tree[right].val)

def nextl(tree,i):
    left=tree[i].l
    return (left,tree[left].val)

layers=list()
for line in x:
    layers.append(line)



treevals=list()
for i in range(len(layers)):
    treevals.append([int(i) for i in layers[i].split(" ")])

tree=list()
for i in range(len(layers)):
    for j in range(len(treevals[i])):
        if(i==len(layers)-1):
            tree.append(Node(treevals[i][j],-1,-1,treevals[i][j]))
        else:
            tree.append(Node(treevals[i][j],len(tree)+i+2,len(tree)+i+1,treevals[i][j]))


#Idea: start at the 2nd to lowest leaf take max of each child and add it to the current node's val
end=sum([len(i) for i in treevals])
for level in range(len(layers)-1,0,-1):
    end-=len(treevals[level])
    start=end-len(treevals[level-1])
    for i in range(start,end):
        tree[i].dist+=max(tree[tree[i].r].dist,tree[tree[i].l].dist)
    #print tree[i].dist

print tree[0].dist

