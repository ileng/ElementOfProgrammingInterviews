#!/usr/bin/env python
# encoding: utf-8

def removeDup(nums):
    n = len(nums)
    ix, write_ix = 1,1
    while ix < n:
        if nums[ix]== nums[write_ix -1]:
            ix += 1
        else:
            nums[write_ix] = nums[ix]
            write_ix += 1
            ix += 1
    return nums


nums = [1, 2, 2, 3, 4, 4]
print(removeDup(nums))


