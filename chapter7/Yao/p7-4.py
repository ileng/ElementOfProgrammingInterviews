#!/usr/bin/env python
# encoding: utf-8

def reverseWords(s):
    word = ''
    res = ''
    for aChar in s:
        if aChar != ' ':
            word += aChar
        else:
            res = word + " " + res
            word = ''
    res = word + ' ' + res
    return  res.strip()

def reverseWords2(s):
    s = list(s)
    s.reverse()
    print(s)
    try:
        start = 0
        while True:
            end = s.index(' ', start)
    #        print(end)
            #s[start:end].reverse()
            start =  end + 1
    except ValueError:
        s[start:].reverse()

    return ''.join(s)



s = 'Alice likes Bob'
print(reverseWords2(s))


