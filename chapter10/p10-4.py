#!/usr/bin/env python
# encoding: utf-8

from tree import *

def getLCA(root, node1, node2):
    if not root or root == node1 or root == node2:
        return root

    rNode1 = isChild(root.right, node1)
    rNode2 = isChild(root.right, node2)

    if rNode1 and rNode2 or (not rNode1 and not rNode2):
        return root
    if rNode1 and not rNode2:
        return getLCA(root.left, node1, node2)
    if not rNode1 and rNode2:
        return getLCA(root.right, node1, node2)



def isChild(root, node):
    if root == node:
        return True
    if not root:
        return False
    return isChild(root.left, node) or isChild(root.right, node)


def getPath(root, node, path):
    if root == node:
        path.append(root.val)
        return
    if not root:
        return None
    getPath(root.left, node, path)
    if path:
        path.append(root.val)
        return path
    getPath(root.right, node, path)
    if path:
        path.append(root.val)
        return path


def getLCA2(root, node1, node2):
    path1 = []
    path2 = []
    getPath(root, node1, path1)
    getPath(root, node2, path2)
    path1 = set(path1)
    for node in path2:
        if node in path1:
            return node

root = testTree
node1 = testTree.left.left
node2 = testTree.left.right


res = getLCA2(root, node1, node2)
print(res)

