"""
    冒泡排序

    两两交换，将大的值往后放。
"""

from typing import List


def bubble_sort(arr: List[int]):
    """
        如果前面的值大于后面的值，则交换位置。
    """
    arr_len = len(arr)

    for i in range(arr_len):
        for j in range(arr_len - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def bubble_sort2(arr):
    """
        在上面的基础上加了一个判断，如果在某一次循环中，没有发生一次交换，则可以提前停止，不需要在往后执行了。
    """
    arr_len = len(arr)

    for i in range(arr_len):
        flag = True
        for j in range(arr_len - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False

        if flag:
            break

    return arr


if __name__ == '__main__':
    arr = bubble_sort([3, 5, 4, 1, 2, 6])
    print(arr)
