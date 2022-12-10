def bubble_sort(arr):
    """ 冒泡排序.

    1. 如果前面的值大于后面的值，则交换位置。
    2. 如果某一次循环没有交换值，则不需要继续循环下去

    Args:
        arr:

    Returns:

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
