#!/usr/bin/env python
# encoding: utf-8

def rnp(s):
    stack = []
    symbls = s.split(', ')
    for each in symbls:
        if each not in '-+*/':
            stack.append(int(each))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if  each == '+':
                stack.append(num1 + num2)
            elif each == '-':
                stack.append(num2 - num1)
            elif each == '*':
                stack.append(num2 * num1)
            else:
                stack.append(num2 / num1)
    return stack[0]


print(rnp('3, 4, +, 2, *, 1, +'))
