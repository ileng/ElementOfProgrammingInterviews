#!/usr/bin/env python
# encoding: utf-8


def getMaxSlideWindow(aList):
    curMax = 0
    res = []
    times = []

    window = []

    for time, val in aList:
        while times and time - times[0] > 3:
            times.pop(0)
            window.pop(0)
        window.append(val)
        times.append(time)

        curMax = max(window)
        res.append((time, curMax))

    return res

aList = [(0, 1.3), (2, 2.5), (3, 3.7), (5, 1.4), (6, 2.6), (8, 2.2), (9, 1.7), (14, 1.1)]

print(getMaxSlideWindow(aList))
