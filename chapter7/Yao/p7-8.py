#!/usr/bin/env python
# encoding: utf-8

def validIps(s):
    res = []
    validIpsHelper(s, 0, res, '', 0)
    return res
def validIpsHelper(s,ix, res, temp, count):
    n = len(s)
    if count == 4 and ix > n:
        return
    if count == 4 and ix == n:
        res.append(str(temp))
        return
    count += 1

    if ix <= n-1:
        validIpsHelper(s, ix+1, res, temp + '.' + s[ix], count)

    if ix <= n - 2:
        validIpsHelper(s, ix + 2, res, temp + '.' + s[ix:ix+2], count)

    if ix <= n- 3  and int(s[ix:ix + 3]) <= 255:
        validIpsHelper(s, ix + 3, res, temp + '.' + s[ix:ix+3], count)


s = '19216811'
print(validIps(s))

