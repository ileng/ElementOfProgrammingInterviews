#!/usr/bin/env python
# encoding: utf-8

def reverseBits(num):
    res = 0
    while num:
        res = res << 1
        res += num & 1
        num = num >> 1

    return res

precomputed_reverse = [0]*(2**16)
for ix in range(2**16):
    precomputed_reverse[ix] = reverseBits(ix)

def reverseBits2(num):
    kWordSize = 16
    kBitMask = 2**16-1
    return precomputed_reverse[num & kBitMask] << 3*kWordSize | \
           precomputed_reverse[num >> kWordSize & kBitMask] << 2*kWordSize | \
           precomputed_reverse[num >> (2*kWordSize) & kBitMask] << kWordSize | \
           precomputed_reverse[num >> (3*kWordSize) & kBitMask]

print(reverseBits(6))
