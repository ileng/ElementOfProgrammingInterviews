#!/usr/bin/env python
# encoding: utf-8

def normalizePath(s):
    if len(s) == 0:
        return None
    res = '/' if s[0] == '/' else ""

    pathNames = s.split('/')
    nameStack = []
    for each in pathNames:
        if each == '..':
            if len(nameStack) == 0:
                return "Error"
            else:
                nameStack.pop()
        elif each == '.' or each == '':
            continue
        else:
            nameStack.append(each)

    for each in nameStack:
        res += each + '/'

    return res



s = '/hi/../ok/.'
print(normalizePath(s))
