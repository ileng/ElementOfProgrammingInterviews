#!/usr/bin/env python
# encoding: utf-8

#test if there's a cycle in the given list
# If there's a cycle, return the reference to that start point else return None
def hasCycle(aList):
    slow = aList
    fast = aList
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        # get the length of the cycle
        if fast == slow:
            len = 1
            slow = slow.next
            while fast != slow:
                slow = slow.next
                len += 1

        # find the start of the cycle
            front = aList
            while len :
                front = front.next
                len -= 1
            end = aList
            while end != front:
                end = end.next
                front = front.next

            return front
    return None
