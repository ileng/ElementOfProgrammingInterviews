#!/usr/bin/env python
# encoding: utf-8

from tree import *

def preOrderTraverse(root):
    res = []
    nodeStack = []
    iter = root
    while iter or nodeStack:
        if not iter:
            iter = nodeStack.pop()
            iter = iter.right
        if iter:
            res.append(iter.val)
            nodeStack.append(iter)
            iter = iter.left
    return res


def posOrderTraverse(root):
    res = []
    nodeStack = []
    iter = root
    while iter or nodeStack:
        if not iter:
            iter = nodeStack.pop()
            if not iter.right:
                res.append(iter.val)
            iter = iter.right
        if iter:
            nodeStack.append(iter)
            iter = iter.left
    return res

print(preOrderTraverse(testTree))
print(posOrderTraverse(testTree))
