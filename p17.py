#!/usr/bin/python
from math import *

numbs={
    0:0,
    1:3,
    2:3,
    3:5,
    4:4,
    5:4,
    6:3,
    7:5,
    8:5,
    9:4,
    10:3,
    11:6,
    12:6,
    13:8,
    14:8,
    15:7,
    16:7,
    17:9,
    18:8,
    19:8,
    20:6,
    30:6,
    40:5,
    50:5,
    60:5,
    70:7,
    80:6,
    90:6,
    100:7,
    1000:8
    }

tot=0
for i in range(1,1001):
    if i<21:
        tot+=numbs[i]
    else:
        ii=str(i)
        leni=len(ii)
        cnt=0
        a=0
        done=0
        for digit in ii:
            place=leni-cnt-1
            if place==0:
                tot+=numbs[int(digit)]
                a+=numbs[int(digit)]
            elif place==1:
                tot+=numbs[int(digit)*10]
                a+=numbs[int(digit)*10]
            elif place==2 and int(digit)>0:
                if (int(ii[2])>0) or (int(ii[1])>0):
                    tot+=3 #for 'and'
                    a+=3
                    if ((int(ii[1])<2) or (int(ii[1])==2 and int(ii[2])==0)):
                        print ii,ii[1],ii[2],ii[1:3]
                        tot+=numbs[int(ii[1:3])]
                        done=1
                tot+=numbs[100]
                tot+=numbs[int(digit)]
                a+=numbs[100]
                a+=numbs[int(digit)]
                if done==1: break
            elif place==3:
                tot+=numbs[1000]
                tot+=numbs[int(digit)]
                a+=numbs[1000]
                a+=numbs[int(digit)]
            cnt+=1
        #print ii,a
print tot


print(len("twohundredandfiftyfive"))
print(len("onethousand"))
print(len("onehundredandeleven"))
