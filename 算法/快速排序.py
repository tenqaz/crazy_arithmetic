"""
    快速排序

    1. 先从数组中选择一个数作为基准值
    2. 将所有比基准值小的放左边，比基准值大的放右边，也就是基准值是放在中间的。
    3. 然后再递归的将基准值左边数组和右边数组再进行排序。
"""


def partition(arr, start_index, end_index):
    mid = arr[end_index]

    p = start_index
    for i in range(start_index, end_index):

        if arr[i] <= mid:
            arr[p], arr[i] = arr[i], arr[p]
            p += 1

    arr[p], arr[end_index] = arr[end_index], arr[p]
    return p


def quick_sort(arr, start_index, end_index):
    """ 快速排序

    Args:
        arr:

    Returns:

    """

    if start_index < end_index:
        p = partition(arr, start_index, end_index)

        quick_sort(arr, start_index, p - 1)
        quick_sort(arr, p + 1, end_index)


if __name__ == '__main__':
    arr = [4, 5, 6, 1, 3, 2]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
