#!/usr/bin/env python
# encoding: utf-8

def lookAndSay(n):
    s = '1'

    for i in range(1, n):
        s = lookAndSayHelper(s)

    return s

def lookAndSayHelper(s):
    if len(s) == 0:
        return ''
    ix = 1
    while ix < len(s) and s[ix]==s[ix-1]:
        ix += 1
    if ix == len(s):
        return str(ix) + s[ix-1]
    else:
        return str(ix) + s[ix-1] + lookAndSayHelper(s[ix:])

def nextNumber(s):
    n = len(s)
    ix = 0
    res = ''
    while ix < n:
        count = 1
        while ix + 1 < n and  s[ix]==s[ix+1]:
            count += 1
            ix += 1
        res += str(count) + s[ix]
        ix += 1
    return res


print(nextNumber('21'))
