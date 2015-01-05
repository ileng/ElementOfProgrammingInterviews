#!/usr/bin/env python
# encoding: utf-8

def findMissPositive(nums):
    n = len(nums)
    res = [0]*(n+1)
    for each in nums:
        if each <= n:
            res[each] = each
    ix = 1
    while ix <= n:
        if res[ix]==0:
            return ix
        ix += 1
    return 1


nums = [1, 3, 5, 9, 4]

print(findMissPositive(nums))
