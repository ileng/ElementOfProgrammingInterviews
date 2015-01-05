#!/usr/bin/env python
# encoding: utf-8

def addOne(digits):
    carry = 0
    n = len(digits)
    for ix in range(n-1, -1, -1):
        if ix == n-1:
            carry, digits[ix] = (carry + 1 + digits[ix]) // 10, (carry + 1 + digits[ix]) % 10
        else:
            carry, digits[ix] = (carry + digits[ix]) // 10, (carry + digits[ix]) % 10
    if carry:
        digits.insert(0,1)



digits = [ 9]

addOne(digits)

print(digits)
