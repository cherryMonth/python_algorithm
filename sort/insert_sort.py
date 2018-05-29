# coding=utf-8

#    插入排序
#    插入排序的思想就是构造一个有序序列，一个无序序列
#    首先从无序序列中取出一个元素放入到有序序列中，找到合适的位置，所有大于该元素的有序元素后移，一直到无序序列为空集


def InsertSort(nums_list):

    for i in range(1, len(nums_list)):  # i - 1  代指当前有序集合最大元素的下标
        if nums_list[i] < nums_list[i-1]:
            temp = nums_list[i]  # 哨兵记录当前无序的元素
            j = i - 1
            while nums_list[j] > temp and j > -1:  # 把这个元素放到有效集合合适的位置 所有大于该元素的下标后移
                nums_list[j+1] = nums_list[j]
                j -= 1
            nums_list[j+1] = temp  # 空闲的位置放入无序的元素


test = [5, 4, 3, 2, 1, 2, 2, 2, 2, 2, -2, 4, 5, 4, 5]
InsertSort(test)
print test


