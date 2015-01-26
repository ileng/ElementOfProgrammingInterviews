#!/usr/bin/env python
# encoding: utf-8

from tree import *

def isSymmetric(root):
    if not root:
        return True

    return isSymmetricHepler(root.left, root.right)

def isSymmetricHepler(left, right):
    if not left and not right:
        return True
    if left and right:
        return left.val == right.val and \
                isSymmetricHepler(left.right, right.left) and \
                isSymmetricHepler(left.left, right.right)
    return False



print(isSymmetric(testTree))
