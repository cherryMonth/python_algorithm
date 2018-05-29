# coding=utf-8

'''
冒泡排序

冒泡与插入排序有本质的不同， 我有一段时间无法区分两者的区别

'''


def bubble_sort(nums_list):
    for i in range(len(nums_list)-1):
        for j in range(len(nums_list)-1):
            if nums_list[j+1] < nums_list[j]:
                temp = nums_list[j]
                nums_list[j] = nums_list[j+1]
                nums_list[j+1] = temp


test = [5, 4, 3, 2, 1, 2, 2, 2, 2, 2, -2, 4, 5, 4, 5]
bubble_sort(test)
print test
