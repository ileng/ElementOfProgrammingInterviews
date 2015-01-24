#!/usr/bin/env python
# encoding: utf-8

from linkedList import *

# check if there's overlap between two linked lists
def getOverlapNode(L1, L2):
    while (L1 and L2 and L1 != L2):
        L1 = L1.next
        L2 = L2.next
    # return None if there's no overlap between L1 and L2
    return L1

def findFistOverlappingNode(L1, L2):
    length1 = getLength(L1)
    length2 = getLength(L2)
    diff = (length1 - length2)

    long = L1 if diff else L2
    short = L2 if diff else L1
    diff = diff if diff else -diff

    print(diff)
    while diff:
        long= long.next
        diff -= 1
    return getOverlapNode(long, short)


def getLength(L):
    length = 0
    while L:
        length += 1
        L = L.next

    return length



if __name__ == "__main__":
    aList = createList(0, 10)
    head = Node(-1)
    head.next = aList
    res = findFistOverlappingNode(head, aList)
    printList(aList)
    printList(head)
    printList(res)
