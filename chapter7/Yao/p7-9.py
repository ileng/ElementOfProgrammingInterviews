#!/usr/bin/env python
# encoding: utf-8

def snakeStraing(s):
    res = ''
    ix = 1
    while ix < len(s):
        res += s[ix]
        ix += 4
    ix = 0
    while ix < len(s):
        res += s[ix]
        ix += 2
    ix = 3
    while ix < len(s):
        res += s[ix]
        ix += 4


    return res

s = 'Hello World'
print(snakeStraing(s))
