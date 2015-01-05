#!/usr/bin/env python
# encoding: utf-8

def sortArray(aList, x):
    n = len(aList)
    ix, jx = 0, n-1
    while ix < jx:
        if aList[ix] >= x:
            aList[ix], aList[jx] = aList[jx], aList[ix]
            jx -= 1
        else:
            ix += 1
    print(ix, jx)
    print(aList)
    ix += 1; jx+= 1
    while jx < n:
        if aList[jx] == x:
            aList[ix], aList[jx] = aList[jx], aList[ix]
            ix += 1
        jx += 1

aList = [5,3,1,2,3]
sortArray(aList, 3)
print(aList)


