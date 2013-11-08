#!/usr/bin/python
from math import *
import itertools

def printGrid(grid):
    for i,line in enumerate(grid):
        if i>0 and i%3==0:
            print "-"*17
        line=" ".join(map(str,line))
        print line[0:5]+"|"+line[6:11]+"|"+line[12:]
    print ""        

def flatten(listOfLists):
    "Flatten one level of nesting"
    return itertools.chain.from_iterable(listOfLists)

def row_valid(v,i,j,grid):
    if v in grid[i]:
        return False
    return True

def col_valid(v,i,j,grid):
    if v in [grid[a][j] for a in range(9)]:
        return False
    return True

def box_valid(v,i,j,grid):
    ip=i/3
    jp=j/3
    box=flatten(map(lambda x:x[jp*3:(jp+1)*3],grid[ip*3:(ip+1)*3]))
    if v in box:
        return False
    return True

def isvalid(v,i,j,grid):
    return row_valid(v,i,j,grid) and \
           col_valid(v,i,j,grid) and \
           box_valid(v,i,j,grid)

def sudokuSolve(grid):
    guesses=[[True]*9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                guesses[i][j]=False

    stop = False
    index=0
    cnt=0
    minval=1
    while index<81:
        i=index/9
        j=index%9

        if guesses[i][j]: 
            index+=1
            continue

        good=False
        for v in range(minval,10):
            if isvalid(v,i,j,grid):
                grid[i][j]=v
                good=True
                break
        minval=1

        if good:
            index+=1
        else:
            grid[i][j]=0
            good=False
            for ti in range(index-1,-1,-1):
                a=ti/9
                b=ti%9
                if guesses[a][b]: continue
                if grid[a][b]<9:
                    good=True
                    index=ti
                    minval=grid[a][b]+1
                    break
                else:
                    grid[a][b]=0
    return 0


#Parse file
data=open("sudoku.txt","r").readlines()
sGrids=list()
for line in data:
    if "Grid" in line:
        sGrids.append(list())
    else:
        sGrids[-1].append(map(int,line.strip()))

#Solve
t=0
for i,grid in enumerate(sGrids):
    print "="*10,i
    printGrid(grid)
    sudokuSolve(grid)
    printGrid(grid)

    t+=grid[0][0]*100+grid[0][1]*10+grid[0][2]
print t


