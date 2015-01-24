#!/usr/bin/env python
# encoding: utf-8

#test if a given bracket sequence is well formed or not

def isWellFormed(s):
    stack = []
    for aBracket in s:
        if aBracket in "({[":
            stack.append(aBracket)
        else:
            if len(stack) == 0:
                return False
            bracket = stack.pop()
            tmp = bracket + aBracket
            if tmp not in ['()', '{}', '[]']:
                return False
    return len(stack) == 0

s = '(){})'
print(isWellFormed(s))
