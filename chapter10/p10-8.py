#!/usr/bin/env python
# encoding: utf-8

from tree import *

def findKthNode(root, k):
    if not root:
        return None
    if root.number < k or k <= 0:
        return None
    if k == 1:
        return root
    if root.left and root.left.number >= k-1:
        return findKthNode(root.left, k - 1)
    else:
        res = 1 if not root.left else root.left.number + 1
        return findKthNode(root.right, k -res)


root = testTree

node = findKthNode(root, 3)
if node:
    print(node.n)
