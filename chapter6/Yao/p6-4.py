#!/usr/bin/env python
# encoding: utf-8

def winGame(nums):
    finalInx = 0
    n = len(nums)
    ix = -1
    while ix < finalInx and ix < n-1:
        ix += 1
        tmp = ix + nums[ix]
        finalInx = max(tmp, finalInx)
    return  finalInx >= n-1


nums = [3,3,1,0,2,0,1]
print(winGame(nums))

