#!/usr/bin/env python
# encoding: utf-8

def encoding(num):
    sBin = bin(num)
    sBin = sBin[2:]
    res = (len(sBin)-1)*'0' + sBin
    return res



print(encoding(13))
