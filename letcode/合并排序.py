# coding=utf-8


def sort(num_list, begin, length):
    temp = []
    mid = (begin + length) / 2
    i = begin
    j = mid
    while i < mid and j < length:
        if num_list[i] < num_list[j]:
            temp.append(num_list[i])
            i += 1
        else:
            temp.append(num_list[j])
            j += 1

    while i < mid:
        temp.append(num_list[i])
        i += 1

    while j < length:
        temp.append(num_list[j])
        j += 1

    j = 0
    for i in range(begin, length):
        num_list[i] = temp[j]
        j += 1


def merge(num_list, begin, length):
    if begin < length - 1:
        mid = (begin + length) / 2
        merge(num_list, begin, mid)
        merge(num_list, mid, length)
        sort(num_list, begin, length)


def merge_sort(num_list):
    if not num_list:
        return list()
    merge(num_list, 0, len(num_list))
    return num_list


import numpy as np
import time
start = time.time()
test1 = np.random.random(size=1000000)
end = time.time()
test = [3, 2, 1]
print merge_sort(test1.tolist())
print end - start