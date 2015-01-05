#!/usr/bin/env python
# encoding: utf-8

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseList(head):
    cur = head;prve = None
    while cur:
        temp = cur
        cur.next = prve
        cur = temp.next
        prve = cur

    return prve
