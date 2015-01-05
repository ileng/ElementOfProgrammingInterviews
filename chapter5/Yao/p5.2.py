#!/usr/bin/env python
# encoding: utf-8

def swapBits(num, i, j):
    ai = (num >> i) & 1
    aj = (num >> j) & 1
    print(ai, aj)
    num -= ai<< i
    num += aj<< i
    num -= aj<< j
    num += ai<< j
    return num

def swapBits2(num, i, j):
    if (num >> i) & 1 != (num >> j) & 1:
        return num ^ ((1<<i) | (1<<j))
    return num

print(swapBits2(6, 0, 1))

