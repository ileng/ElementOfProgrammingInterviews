#!/usr/bin/env python
# encoding: utf-8

def sortArray(nums, pivot_ix):
    smaller, equal = 0, 0
    larger = len(nums) -1
    pivot = nums[pivot_ix]
    while equal < larger:
        if nums[equal] < pivot:
            nums[smaller], nums[equal] = nums[equal], nums[smaller]
            smaller += 1; equal += 1
        elif nums[equal] > pivot:
            nums[equal], nums[larger] = nums[larger], nums[equal]
            equal += 1; larger -= 1
        else:
            equal += 1


nums = [1, 3, 2, 2, 5, 4, 3]
sortArray(nums, 1)
print(nums)

