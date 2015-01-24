#!/usr/bin/env python
# encoding: utf-8

def shortestStraightLine(num):
    queue = []
    queue.append([1])
    while queue:
        nums = queue.pop(0)
        for aNum in nums:
            last = nums[-1]
            if last + aNum > num:
                continue
            tmp = list(nums)
            tmp.append(last + aNum)
            if last + aNum == num:
                return tmp
            queue.append(tmp)


print(shortestStraightLine(15))

