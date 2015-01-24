#!/usr/bin/env python
# encoding: utf-8

def printTreeDepth(root):
    if not root:
        return
    queue = [root]
    while queue:
        curNode = queue.pop(0)
        print(curNode.val)
        if curNode.left:
            queue.append(curNode.left)
        if curNode.right:
            queue.append(curNode.right)

class TreeNode:
    def __init__(self, x):
        self.val  = x
        self.left = None
        self.right = None

root = TreeNode(314)
root.left = TreeNode(26)
root.right = TreeNode(26)
root.left.left = TreeNode(271)
root.left.right = TreeNode(56)

printTreeDepth(root)
