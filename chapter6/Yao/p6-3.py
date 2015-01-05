#!/usr/bin/env python
# encoding: utf-8

def strProduct(s1, s2):
    sign = 1

    if s1[0] == '-':
        sign = -sign
        s1 = s1[1:]
    if s2[0] == '-':
        sign = -sign
        s2 = s2[1:]

    s1 = list(s1)
    s1.reverse()
    s2 = list(s2)
    s2.reverse()

    m,n = len(s1), len(s2)

    res = [0]*(m + n)
    for ix in range(0, m):
        for jx in range(0, n):
            res[ix + jx] += int(s1[ix])*int(s2[jx])
            res[ix + jx + 1] += res[ix + jx] // 10
            res[ix + jx] %= 10
    res.reverse()
    res = [str(i) for i in res]
    res = ''.join(res)
    ix = 0
    while ix < m + n-1 and res[ix]=='0':
        ix += 1

    res = res[ix:]
    if sign < 0:
        res = '-' + res
    return res


s1 = '-130'
s2 = '10'
print(strProduct(s1,s2))


