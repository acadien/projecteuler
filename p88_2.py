#!/usr/bin/python

curreNs=dict()

ks=range(2,12000)
bigN=24000
cSets={k:[2*k] for k in range(2,bigN)}



for i1 in range(2,bigN):
    upper2=bigN/i1+1
    for i2 in range(i1,upper2):
        N2=i1*i2
        S2=i1+i2
        a=N2-S2+2
        cSets[a]=min([cSets[a],N2]) #2 number solutions!
        
        upper3=upper2/i2+1
        for i3 in range(i2,upper3):
            N3=N2*i3
            S3=S2+i3
            a=N3-S3+3
            cSets[a]=min([cSets[a],N3])

            upper4=upper3/i3+1
            #if i3>upper4:continue
            print i3,upper4
            for i4 in range(i3,upper4):
                N4=N3*i4
                S4=N3+i4
                a=N4-S4+4
                if a==12:# and cSets[a]>N4:
                    print i1,i2,i3,i4
                cSets[a]=min([cSets[a],N4])
            
            
for i in range(2,20):
    print i,cSets[i]
#print cSets[8],12
#print cSets[11],16
#print cSets[268],288
#print cSets[269],360
