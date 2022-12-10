def insert_sort(arr):
    """ 插入排序

    Args:
        arr:

    Returns:

    """

    arr_len = len(arr)

    for i in range(1, arr_len):

        val = arr[i]

        for j in range(i - 1, -2, -1): 
            if val < arr[j]:
                arr[j + 1] = arr[j]
            else:
                break

        arr[j+1] = val

    return arr


if __name__ == '__main__':
    arr = insert_sort([4, 5, 6, 1, 3, 2])
    print(arr)