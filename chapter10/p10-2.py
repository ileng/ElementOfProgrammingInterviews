#!/usr/bin/env python
# encoding: utf-8

from tree import *

def findKBalanced(root, k):
    return findKBalancedHelper(root, k)

def findKBalancedHelper(root, k) :
    if not root:
        return (None, 0)

    left_result = findKBalancedHelper(root.left, k)
    if left_result[0]:
        return (left_result[0], 0)

    right_result = findKBalancedHelper(root.right, k)
    if right_result[0]:
        return (right_result[0], 0)

    node_num = left_result[1] + right_result[1] + 1

    if abs(left_result[1] - right_result[1]) > k:
        return (root.val, node_num)

    return (None, node_num)



print(findKBalanced(testTree, 1))

