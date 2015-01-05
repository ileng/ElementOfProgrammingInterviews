#!/usr/bin/env python
# encoding: utf-8

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


def reverseRange(head, start, end):
    prev = None
    cur = head; ix = 0
    while ix < start:
        prev = cur
        cur = cur.next

        ix += 1
    while ix < end:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

        ix += 1
    return head
