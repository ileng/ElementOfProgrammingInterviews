#!/usr/bin/env python
# encoding: utf-8

maps = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', \
        6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
def number2Words(res, nums, aList):
    if len(nums)==0:
        aList.append(res)
        return

    num = int(nums[0])
    for each in maps[num]:
        number2Words(res + each, nums[1:], aList)

nums = '2276696'
aList = []
number2Words('', nums, aList)
print(aList)


