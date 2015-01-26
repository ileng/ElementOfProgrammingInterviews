#!/usr/bin/env python
# encoding: utf-8
from tree import *

def isBalanced(root):
    if not root:
        return True
    lh = getHeight(root.left)
    rh = getHeight(root.right)

    maxH, minH = max(lh, rh), min(lh, rh)

    return maxH <= minH + 1


def getHeight(root):
    if not root:
        return 0
    return max(getHeight(root.left), getHeight(root.right)) + 1



print(isBalanced(testTree))
