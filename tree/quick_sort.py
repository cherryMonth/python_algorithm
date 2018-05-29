# coding=utf-8
import numpy as np


def quick_sort(nums_list):
    if len(nums_list) < 2:
        return nums_list

    temp = nums_list[0]
    left = [num for num in nums_list[1:] if num < temp]
    right = [num for num in nums_list[1:] if num >= temp]

    return quick_sort(left) + [temp] + quick_sort(right)


print quick_sort(np.random.random(size=10))
