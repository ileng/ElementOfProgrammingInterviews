#!/usr/bin/env python
# encoding: utf-8

from tree import *

def getSum(root):
    if not root:
        return 0
    res = root.val
    if not root.left:
        res *= 2
    if not root.right:
        res *= 2

    return res  + getSum(root.left) + getSum(root.right)

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.right.right = TreeNode(1)


print(getSum(root))


