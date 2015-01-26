#!/usr/bin/env python
# encoding: utf-8

from tree import *

def pathToSpecifiedSum(root, n):
    path = []
    if foundPath(root, n, path):
        return path
    return []



def foundPath(root, n, path):
    if not root:
        path = []
        return False
    if not root.left and not root.right:
        if root.val == n:
            path.append(root.val)
            return True
        else:
            path = []
            return False

    if foundPath(root.left, n - root.val, path):
        path.append(root.val)
        return True
    if foundPath(root.right, n - root.val, path):
        path.append(root.val)
        return True




root = testTree
print(pathToSpecifiedSum(root, 320))
