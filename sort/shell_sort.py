# coding=utf-8

import math

'''
    希尔排序
    由简单插入排序的原理我们知道，插入排序的效率随着数组的有序度增强而提高
    所以我们通过最大步长来构造相对有序的子序列，此时逐渐减低步长，因为当前数组相对有序，所以效率会提高，直到减少步长为1
'''


def shell_insert_sort(nums_list, dk):  # dk 代表当前的步长 即插入元素的下标间隔 为1时即为简单插入排序
    for i in range(dk, len(nums_list)):  # i - dk  代指当前有序集合最大元素的下标
        if nums_list[i] < nums_list[i-dk]:
            temp = nums_list[i]  # 记录当前无序的元素
            j = i - dk
            while nums_list[j] > temp and j > -1:  # 把这个元素放到有效集合合适的位置 所有大于该元素的下标后移
                nums_list[j+dk] = nums_list[j]
                j -= dk
            nums_list[j+dk] = temp  # 空闲的位置放入无序的元素


def shell_sort(num_list):
    t = int(math.log(len(num_list), 2))  # 找到最大的趟数
    dlta = list()
    for k in range(1, t + 1):  # 生成步长序列
        dlta.append(2**(t-k+1)-1)

    for dk in dlta:
        shell_insert_sort(num_list, dk)
        print num_list


test = [5, 4, 3, 2, 1, 2, 2, 2, 2, 2, -2, 4, 5, 4, 5]
shell_sort(test)
