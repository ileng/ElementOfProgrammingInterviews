#!/usr/bin/env python
# encoding: utf-8

class Node:
    def __init__(val):
        self.val = val
        self.next = None

def mergeLists(l, f):
    res = Node()
    cur = res
    while l.next and f.next:
        if l.next.val < f.next.val:
            cur.next = l.next
            l = l.next
        else:
            cur.next = f.next
            f= f.next
        cur = cur.next

    if not l.next:
        cur.next = l.next
    elif not f.next:
        cur.next = f.next

    return res


