#!/usr/bin/env python
# encoding: utf-8

def getParity(number):
    res = 0

    while number:
        res ^= number & 1
        number >>= 1

    return res

number = 7
print(getParity(number))
