# coding=utf-8

'''
选择排序
'''


def select_sort(nums_list):
    for i in range(len(nums_list)-1):
        k = i  # 记录当前下标
        for j in range(i+1, len(nums_list)):  # 从 i+1 到 length 寻找小于给定下标的元素
            if nums_list[j] < nums_list[k]:
                k = j
        if k != i:
            temp = nums_list[i]
            nums_list[i] = nums_list[k]
            nums_list[k] = temp


test = [5, 4, 3, 2, 1, 2, 2, 2, 2, 2, -2, 4, 5, 4, 5]
select_sort(test)
print test