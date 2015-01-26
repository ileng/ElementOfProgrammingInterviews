#!/usr/bin/env python
# encoding: utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

testTree = TreeNode(314)
testTree.left = TreeNode(6)
testTree.right = TreeNode(16)
#testTree.left.left = TreeNode(27)
#testTree.right.right= TreeNode(271)
#testTree.left.right = TreeNode(20)
