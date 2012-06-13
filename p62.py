#!/usr/bin/python

thedict={}
for i in range(1,10000):
    try:
        thedict["".join(sorted(str(i**3)))].append(i**3)
    except KeyError:
        thedict["".join(sorted(str(i**3)))]=[i**3]

print min([min(val) for key,val in thedict.iteritems() if len(val)>=5])

