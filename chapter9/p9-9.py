#!/usr/bin/env python
# encoding: utf-8

def sortStack(stack):
    if len(stack) > 0:
        val = stack[-1]
        stack.pop()
        sortStack(stack)
        insertStack(stack, val)
def insertStack(stack, val):
    if len(stack) > 0:
        if stack[-1] < val:
            stack.append(val)
        else:
            e = stack[-1]
            stack.pop()
            insertStack(stack, val)
            stack.append(e)

    else:
        stack.append(val)


stack = [1, 2, 3, 0, 9, 4, 3]

sortStack(stack)
print(stack)
