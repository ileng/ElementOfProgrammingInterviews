#!/usr/bin/env python
# encoding: utf-8

def canView(aList):
    heights = []
    for height in aList:
        while len(heights) > 0 and heights[-1] < height:
            heights.pop()
        heights.append(height)
    print(heights)


aList = [10, 15, 13, 12]

canView(aList)
