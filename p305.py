#!/usr/bin/python
from math import *
import sys

#Returns a string made of the numbers from num to num+JUMP
def fetch(num,JUMP):
    strn=""
    for i in range(num,num+JUMP):
        strn+=str(i)
    return strn

#Finds all instances of a string val in string snums and returns the number
#if instances and the index of the last index
def findall(snums,val,fcnt):
    maxfcnt=int(val)-fcnt
    incrindex=0
    found=0
    cnt=0
    while cnt<maxfcnt:
        found=snums.find(val,incrindex)
        if found<0:
            break
        else:
            cnt+=1
            incrindex=found+1
    return [cnt,incrindex]

def testfindall(snums,val):
    incrindex=0
    found=0
    incrfcnt=0
    while True:
        found=snums.find(val,incrindex)
        if found<0:
            break
        else:
            incrfcnt+=1
            incrindex=found+1
    return (incrfcnt,incrindex)

#Calculates the number instances of in hop to hop+Jump
def smartfetch(hop,JUMP,val,skip):
    fnd=0 #the number of digits in val that are in hop
    loc=0
    for (i,digit1) in enumerate(skip):
        for digit2 in str(hop)[loc:]:
            if digit1!=digit2:
                break
        if i in str(hop):
            print i,hop
            fnd+=1
            break
    exit(0)
    #Debug
    nums=fetch(hop,JUMP)
    (testincrfcnt,testincrindex)=testfindall(nums,n)

    #Guessed
    incrindex=len(n)*JUMP
    incrfcnt=(20+fnd*100)

    print "hop: ",hop
    print "fcnttest: ",testincrfcnt,incrfcnt
    print "indextest: ",testincrindex,incrindex

    return (incrfcnt,incrindex,hop+JUMP)


#ns=[str(3**k) for k in range(10,14)]
#f=1728200395
ns=[str(3**k) for k in range(1,14)]
f=0
for n in ns:
    n=str(sys.argv[1])
    #INITIALIZE
    nn=int(n)
    nums=""
    fcnt=0
    hop=0
    index=-1
    JUMP=10**(len(n)+2)

    ############################
    #FIND THE FIRST SET OF NUMS#
    ############################
    while fcnt<nn:
        nums+=fetch(hop,JUMP)
        [incrfcnt,incrindex]=findall(nums,n,fcnt)
        fcnt+=incrfcnt
        hop+=JUMP
        index+=incrindex
        nums=nums[incrindex:]
        #print fcnt
    break
    ######################################
    #If Necessary Prepare for Smart Search
    ######################################
    """
    skip=list()
    if fcnt<nn:
        for i in n:
            #if i=="0": continue
            skip.append(i)
    
        while True:
            print "ohboy"
            (incrfcnt,incrindex,newhop)=smartfetch(hop,JUMP,n,skip)
            if fcnt+incrfcnt>nn:
                nums+=fetch(hop,JUMP)
                (fcnt,incrindex)=findall(nums,n,fcnt)
                index+=incrindex
                break
            hop=newhop
            index+=incrindex
            fcnt+=incrfcnt
            if fcnt==nn:
                break
    break
    """
print index
