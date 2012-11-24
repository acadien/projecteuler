#!/usr/bin/python
from math import *



evens=["0","2","4","6","8"]
def isReverse(num,snum):
    sval=str(num+int(snum[::-1]))
    for e in evens:
        if e in sval:
            return False
    return True

#for maxnum in enumerate([10,100,1000,10000,100000,1000000]):
minnum=90000000
maxnum=100000000
cnt=0
#saved=list()
n=len(str(minnum))
for num in range(minnum,maxnum):
    snum=str(num)
    if snum[-1]=="0":
        continue
#    for i in range(n/2):
#        if int(snum[i])%2==int(snum[n-i-1])%2:
#            continue
    if isReverse(num,snum):
#        saved.append(num)
        cnt+=1
#print saved
print cnt


#10E0 - 10E1: 0
#10E1 - 10E2: 20
#10E2 - 10E3: 100
#10E3 - 10E4: 600
#10E4 - 10E5: 0

#1*10E5 - 2*10E5: 3600
#2*10E5 - 3*10E5: 3600
#3*10E5 - 4*10E5: 2700
#4*10E5 - 5*10E5: 2700
#5*10E5 - 6*10E5: 1800
#6*10E5 - 7*10E5: 1800
#7*10E5 - 8*10E5: 900
#8*10E5 - 9*10E5: 900
#9*10E5 - 1*10E6: 0
#10E5 - 10E6: 18000 


#1*10E6 - 2*10E6: 0
#2*10E6 - 3*10E6: 2500
#3*10E6 - 4*10E6: 2500
#4*10E6 - 5*10E6: 5000
#5*10E6 - 6*10E6: 5000
#6*10E6 - 7*10E6: 7500
#7*10E6 - 8*10E6: 7500
#8*10E6 - 9*10E6: 10000
#9*10E6 - 1*10E7: 10000
#10E6 - 10E7: 50000


#1*10E7 - 2*10E7: 108000
#2*10E7 - 3*10E7: 108000
#3*10E7 - 4*10E7: 81000
#4*10E7 - 5*10E7: 81000
#5*10E7 - 6*10E7: 54000
#6*10E7 - 7*10E7: 54000
#7*10E7 - 8*10E7: 27000
#8*10E7 - 9*10E7: 27000
#9*10E7 - 1*10E8: 0
#10E7 - 10E8: 540000

#Total: 608720
