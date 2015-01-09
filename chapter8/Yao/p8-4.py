#!/usr/bin/env python
# encoding: utf-8


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

#Take a singly linked list as input and a nonegative integer k and reverse the k nodes at a time
def reverseList(aList, k):
    iter = aList
    startPtr = iter
    dummyHead = Node(0)
    dummyHead.next = startPtr
    prev = dummyHead
    count  = 1
    while iter:
        if count % k == 0:
            endPtr = iter
            ptr = prev.next
            head, tail = reverse(startPtr, endPtr.next)
            prve.next = head;tail.next = iter.next
            startPtr = endPtr.next
        k += 1
        iter = iter.next
    return dummyHead.next

# reverser the nodes from start pointers to end pointer, exclusivelly.
def reverse(startPtr, endPtr):
    dummyHead= Node(0)
    dummyHead.next = startPtr
    iter = dummyHead.next
    tail = iter
    while iter and iter.next:
        temp = iter.next
        iter.next = temp.next
        temp.next = dummyHead.next
        dummyHead.next = temp
    return dummyHead.next, tail

if __name__ == "__main__":
    aList = Node(0)
    iter = aList
    for i in range(1, 10):
        iter.next = Node(i)
        iter = iter.next
    tail = iter
    aList = reverseList(aList, 3)
    #aList, tail = reverse(aList, tail)

    iter = aList
    while iter:
        print(iter.val, end=" ")
        iter = iter.next



