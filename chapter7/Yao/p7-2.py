#!/usr/bin/env python
# encoding: utf-8

def replaceAndRemove(s):
    res = ''
    for aChar in s:
        if aChar == 'a':
            res += 'dd'
        elif aChar != 'b':
            res += aChar

    return res


def replaceAndRemove2(strList):
    curIndex = 0
    a_count = 0
    for aChar in strList:
        if aChar != 'b':
            strList[curIndex] = aChar
            curIndex += 1
        if aChar == 'a':
            a_count += 1
    n = curIndex + a_count




s = 'abcd'
print(replaceAndRemove(s))
