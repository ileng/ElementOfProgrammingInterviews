#!/usr/bin/env python
# encoding: utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

def inOrderTraverse(root):
    res = []
    iter = root
    while iter:
        if iter.left and iter.left not in res:
            iter = iter.left
        else:
            res.append(iter.val)
            print(res)
            if iter.right and iter.right not in res:
                iter = iter.right
            else:
                while iter.val in res:
                    iter = iter.parent
    return res


root = TreeNode(0)
root.left = TreeNode(1)
root.left.parent = root
root.right = TreeNode(2)
root.right.parent = root

print(inOrderTraverse(root))

