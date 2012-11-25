#!/usr/bin/python

rom2dec={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
ord_rom1=["I","X","C","M"]
ord_rom5=["V","L","D"]
rdvals=[i for i in reversed(sorted(rom2dec.values()))]
rdkeys=[i for i in reversed(sorted(rom2dec.keys(),key=rom2dec.__getitem__))]
def make_roman(val):
    num=""
    sval=reversed(str(val))
    for i,sv in enumerate(sval):
        v=int(sv)
        if i==3:
            toadd="M"*v
        else:    
            if v==0:
                continue
            elif v<4: #1,2,3
                toadd=ord_rom1[i]*v
            elif v<5: #4
                toadd=ord_rom1[i]+ord_rom5[i]
            elif v<6: #5
                toadd=ord_rom5[i]
            elif v<9: #6,7,8
                toadd=ord_rom5[i]+ord_rom1[i]*(v-5)
            else:     #9
                toadd=ord_rom1[i]+ord_rom1[i+1]
        num=toadd+num
    return num

def reduce_roman(num):
    num=num.strip()
    val=[rom2dec[i] for i in reversed(num)]
    fail=1
    while fail==1:
        fail=0
        for i,v1,v2 in zip(range(len(val)-1),val[:-1],val[1:]):
            if v2<v1:
                fail=1
                break
        if fail==1:
            val.pop(i)
            val.pop(i)
            val.insert(i,v1-v2)
            

    val=sum(val)
    newnum=make_roman(val)
    print num,val,newnum
    return len(num)-len(newnum)


            

cnt=0
for numeral in open("roman.txt","r").readlines():
    cnt+=reduce_roman(numeral)
    
print cnt
