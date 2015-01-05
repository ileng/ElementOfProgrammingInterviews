#!/usr/bin/env python
# encoding: utf-8

def isPalindrome(s):
    n = len(s)
    ix = 0;rix = n-1;
    while ix < rix:
        if s[ix]!=s[rix]:
            return False
        ix +=1
        rix -= 1
    return True

s = 'abcba'
s2='abda'
print(isPalindrome(s))
print(isPalindrome(s2))
