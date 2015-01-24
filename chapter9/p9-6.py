#!/usr/bin/env python
# encoding: utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right= None

def printBST(root):
    nodeStack = []
    values = []

    curNode = root
    while curNode or nodeStack:
        if curNode:
            nodeStack.append(curNode)
            curNode = curNode.left
        else:
            curNode = nodeStack.pop()
            values.append(curNode.val)
            curNode = curNode.right

    return (values)


root = TreeNode(35)
root.left = TreeNode(23)
root.right= TreeNode(49)
print(printBST(root))

