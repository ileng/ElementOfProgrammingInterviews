#!/usr/bin/env python
# encoding: utf-8

def computePower(x, y):
    tmp, res = x, 1
    while y!=1:
        if y % 2:
            res *= tmp
        tmp *= tmp
        y = y // 2
    return res*tmp

print(computePower(2, 5))
