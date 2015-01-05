#!/usr/bin/env python
# encoding: utf-8

def int2str(num):
    is_false = True if num < 0 else False
    num = -num if is_false else num
    res = ''
    while num:
        res = str(num % 10) + res
        num = num//10
    return '-' + res if is_false else res

def str2int(s):
    is_false = True if s[0]=='-' else False
    i = 0 if not is_false else 1
    res = 0
    for ix in range(i, len(s)):
        res  = res*10 + (ord(s[ix]) - ord('0'))

    return -res if is_false else res


s = '-1314'
print(str2int(s))
num = -1314
print(int2str(num))

