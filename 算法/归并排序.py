"""

将两个有序数组合并
"""
import math


def merge_sort(arr):
    """ 归并排序

    Args:
        arr:

    Returns:

    """
    if len(arr) < 2:
        return arr

    mid = math.floor(len(arr) / 2)
    left, right = arr[:mid], arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    if left:
        res.extend(left)

    if right:
        res.extend(right)

    return res


if __name__ == '__main__':
    arr = merge_sort([4, 5, 6, 1, 3, 2])
    print(arr)
