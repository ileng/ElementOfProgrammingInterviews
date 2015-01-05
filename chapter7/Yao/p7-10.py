#!/usr/bin/env python
# encoding: utf-8

def rLEcoding(s):
    ix = 0
    res = ''
    while ix+1 < len(s):
        a_count = 1
        while ix + 1 < len(s) and s[ix] == s[ix+1]:
            a_count += 1
            ix += 1
        res += str(a_count) + s[ix]
        ix += 1
    return res

def rLEdecoding(s):
    res = ''
    for ix in range(0, len(s), 2):
        res += int(s[ix])*s[ix+1]
    return res

s = 'eeeffffee'
print(rLEcoding(s))
print(rLEdecoding(rLEcoding(s)))
