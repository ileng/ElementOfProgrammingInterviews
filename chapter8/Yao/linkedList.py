#!/usr/bin/env python
# encoding: utf-8

# define the Node class and provide functions to create and print a linked list
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

def createList(a, b):
    aList = Node(a)
    iter = aList
    for i in range(a + 1, b):
        iter.next = Node(i)
        iter = iter.next
    return aList

def printList(aList):
    iter = aList
    while iter:
        print(iter.value, end = " ")
        iter = iter.next
    print()

