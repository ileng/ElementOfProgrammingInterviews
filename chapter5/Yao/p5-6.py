#!/usr/bin/env python
# encoding: utf-8

def computeQuotient(x, y):
    res = 0
    temp = 1
    while x > y:
        y <<= 1
        temp <<=1

    while x:
        while x < y:
            y >>= 1
            temp >>= 1
        res += temp
        x -= y
    return res


print(computeQuotient(5, 2))
