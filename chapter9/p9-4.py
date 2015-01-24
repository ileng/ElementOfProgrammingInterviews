#!/usr/bin/env python
# encoding: utf-8


def longestMatchedParens(s):
    n = len(s)
    parenStack = []
    maxMatchedLen = 0; end = -1
    for index in range(n):
        if s[index] == '(':
            parenStack.append(index)
        elif len(parenStack) == 0:
            end = index
        else:
            parenStack.pop()
            start = end if len(parenStack) == 0 else parenStack[-1]
            maxMatchedLen = max(maxMatchedLen, index - start)

    return maxMatchedLen



s = "()())()(()"
print(longestMatchedParens(s))

