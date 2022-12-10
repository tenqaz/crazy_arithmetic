"""
@author: Jim
@project: crazy_arithmetic
@file: 240_搜索矩阵2.py
@time: 2021/9/20 13:22
@desc:  
    https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right - left) // 2 + left

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        """ 二分法查找, 对矩阵的每一行进行二分法查找。

        时间复杂度: O(nlogn)
        空间复杂读: O(1)
        """
        matrix_len = len(matrix)
        for i in range(matrix_len):
            mid = self.search(matrix[i], target)

            if mid != -1:
                return True

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """ 从左下角开始搜索，如果比target大，则往上移动，如果比target小，则往右搜索，都不符合，则返回False

            推荐

            时间复杂度: O(i+j2)
            空间复杂度: O(1)
        """
        min_row = 0
        max_row = len(matrix) - 1
        min_col = 0
        max_col = len(matrix[0]) - 1

        i, j = max_row, min_col

        while i >= min_row and j <= max_col:

            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True

        return False


# rst = true
# matrix = [
#     [1, 4, 7, 11, 15],
#     [2, 5, 8, 12, 19],
#     [3, 6, 9, 16, 22],
#     [10, 13, 14, 17, 24],
#     [18, 21, 23, 26, 30]]
# target = 5

# False
# matrix = [[-5]]
# target = -2

# True
matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 20

s = Solution()
ret = s.searchMatrix(matrix, target)
print(ret)
