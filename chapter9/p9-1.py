#!/usr/bin/env python
# encoding: utf-8

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Stack:
    def __init__(self):
        self.max =  None
        self.size = 0
        self.top = None

    def isEmpty(self):
        return self.size == 0

    def getMax(self):
        return self.max

    def push(self, x):
        if not self.top:
            node = Node(x)
            self.max = x
        else:
            node = Node(self.max - x)
            self.max = max(self.max, x)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if not self.top:
            return None
        if not self.top.next:
            return self.top.val
        self.top = self.top.next
        val = self.max if self.top.val < 0 else self.max - self.top.val

        if self.top.val  < 0:
            self.max = self.max + self.top.val

        return val


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.getMax())
print(stack.pop())
print(stack.getMax())


