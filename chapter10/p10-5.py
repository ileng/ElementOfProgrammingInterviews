#!/usr/bin/env python
# encoding: utf-8

def getDepth(node):
    depth = 0
    while node:
        depth += 1
        node = node.parent
    return depth


def getLCA(node0, node1):
    depth0 = getDepth(node0)
    depth1 = getDepth(node1)

    iterMax = node0;iterMin = node1

    if depth0 < depth1:
        iterMax, iterMin = node1, node0

    depth_diff = abs(depth0 - depth1)

    while depth_diff:
        iterMax = iterMax.parent
        depth_diff -= 1

    while iterMax != iterMin:
        iterMax = iterMax.parent
        iterMin = iterMin.parent
    return iterMax

