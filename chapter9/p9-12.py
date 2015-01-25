#!/usr/bin/env python
# encoding: utf-8

class Queue:
    def __init__(self):
        self.stack = []
        self.top = None
        self.back = None


    def enqueue(self, x):
        self.stack.append(x)

    def dequeue(self):
        if len(self.stack) == 1:
            return self.stack.pop()
        tmp = self.stack.pop()
        res = self.dequeue()
        self.stack.append(tmp)
        return res


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
