#!/usr/bin/python

tot=1
for i in range(2,21):
    if tot%i!=0:
        tot*=i
large=tot
i=2
while tot>1:
    if tot%i==0:
        tot/=i
    else:
        i+=1


print large/24
