#!/usr/bin/python
from math import *

x="75x\
95 64x\
17 47 82x\
18 35 87 10x\
20 04 82 47 65x\
19 01 23 75 03 34x\
88 02 77 73 07 63 67x\
99 65 04 28 06 16 70 92x\
41 41 26 56 83 40 80 70 33x\
41 48 72 33 47 32 37 16 94 29x\
53 71 44 65 25 43 91 52 97 51 14x\
70 11 33 28 77 73 17 78 39 68 17 57x\
91 71 52 38 17 14 91 43 58 50 27 29 48x\
63 66 04 68 89 53 67 30 73 16 69 87 40 31x\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

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

layers=x.split("x")

treevals=list()
for i in range(len(layers)):
    treevals.append([int(i) for i in layers[i].split(" ")])

#print treevals[3]
tree=list()
Q=list()
for i in range(len(layers)):
    for j in range(len(treevals[i])):
        if(i==len(layers)-1):
            tree.append(Node(treevals[i][j],-1,-1,treevals[i][j]))
        else:
            tree.append(Node(treevals[i][j],len(tree)+i+2,len(tree)+i+1,treevals[i][j]))
"""
def checkpath(tree,root):
    path=list()
    cur=root
    while(True):
        (cr,crval)=nextr(tree,cur)
        (cl,clval)=nextl(tree,cur)
        if(cr!=-1):    
            tree[cr].dist=crval+tree[cur].dist
            tree[cl].dist=clval+tree[cur].dist
            if(tree[cr].dist>tree[cl].dist):
                cur=cr
            else:
                cur=cl
        else:
            break
    return tree[cur].dist

def checklr(tree,root):
    r=checkpath(tree,tree[root].r)
    l=checkpath(tree,tree[root].l)
    if r>l:
        return (nextr(tree,root),'r')
    return (nextl(tree,root),'l')
    
#Dijkstra's
cur=0
tot=0
while(cur!=-1):
    tot+=tree[cur].val
    print tot
    ((cur,val),dirn)=checklr(tree,cur)
    print dirn
print tot
"""

#Idea: start at the 2nd to lowest leaf take max of each child and add it to the current node's val
end=sum([len(i) for i in treevals])
for level in range(len(layers)-1,0,-1):
    end-=len(treevals[level])
    start=end-len(treevals[level-1])
    for i in range(start,end):
        tree[i].dist+=max(tree[tree[i].r].dist,tree[tree[i].l].dist)
    #print tree[i].dist

print tree[0].dist

"""
end=sum([len(i) for i in treevals])-len(treevals[-1])
start=end-len(treevals[-2])
for i in range(start,end):
    tree[i].dist+=max(tree[tree[i].r].dist,tree[tree[i].l].dist)
    print tree[i].dist
"""
    
        
