#!/usr/bin/env python
# encoding: utf-8

def multiply(a, b):
    res = 0
    while b:
        if b & 1:
            res = add(res, a)
        b >>= 1
        a <<= 1
    return res

def add(a, b):
    res,  k = 0, 1
    temp_a, temp_b = a, b
    carryin, carryout = 0, 0
    while temp_a or temp_b:
        ak, bk = a & k, b & k
        carryout =  (ak & bk) | (ak & carryin) | (bk & carryin)
        res |= (ak ^ bk ^ carryin)
        carryin = carryout << 1
        k <<= 1
        temp_a >>= 1; temp_b >>= 1
    return res | carryin

print(multiply(5, 5))
