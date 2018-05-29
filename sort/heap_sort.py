# coding=utf-8

'''
堆排序
'''


def recursion_head_adjust(nums_list, index, heapsize):  # 递归调整一个数组为大顶堆

    '''
    堆排序中 index 为堆顶元素 heapsize 为堆大小
    :param nums_list:
    :param index:
    :param heapsize:
    :return:
    '''

    _max = index
    left = 2 * index + 1
    right = 2 * (index + 1)

    if left < heapsize and nums_list[left] > nums_list[_max]:
        _max = left
    if right < heapsize and nums_list[right] > nums_list[_max]:
        _max = right

    if _max != index:  # 对子节点进行递归调整
        temp = nums_list[_max]
        nums_list[_max] = nums_list[index]
        nums_list[index] = temp
        recursion_head_adjust(nums_list, _max, heapsize)


def head_adjust(nums_list, index, heapsize):

    while True:
        _max = index
        left = 2 * index + 1
        right = 2 * (index + 1)

        if left < heapsize and nums_list[left] > nums_list[_max]:
            _max = left
        if right < heapsize and nums_list[right] > nums_list[_max]:
            _max = right

        if _max != index:
            temp = nums_list[_max]
            nums_list[_max] = nums_list[index]
            nums_list[index] = temp
            index = _max
        else:
            break


def head_sort(nums_list):
    length = len(nums_list)
    i = length/2 - 1
    while i >= 0:  # 构建大顶堆 每次调整后会出现变动 所以需要重新调整
        head_adjust(nums_list, i, length)
        i -= 1

    i = length - 1
    while i > 0:
        temp = nums_list[0]
        nums_list[0] = nums_list[i]
        nums_list[i] = temp
        head_adjust(nums_list, 0, i)  # 每次调整都会出现一个最大的元素 缩小排序范围
        i -= 1


test = [5, 4, 3, 2, 1, 2, 2, 2, 2, 2, -2, 4, 5, 4, 5]
head_sort(test)
print test
