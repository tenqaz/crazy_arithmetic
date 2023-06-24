"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/24 12:27
@desc:
    https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/?envType=study-plan-v2&envId=coding-interviews
"""
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        column_len = len(matrix[0])
        row_len = len(matrix)

        row = 0
        column = 0
        for i in range(column_len):
            if matrix[row][i] == target:
                return True

            if matrix[row][i] > target:
                column = i - 1
                break
        else:
            column = i

        for j in range(row_len):
            if matrix[j][column] == target:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    # data = [
    #     [1, 4, 7, 11, 15],
    #     [2, 5, 8, 12, 19],
    #     [3, 6, 9, 16, 22],
    #     [10, 13, 14, 17, 24],
    #     [18, 21, 23, 26, 30]
    # ]
    #
    # ret = s.findNumberIn2DArray(data, 20)
    ret = s.findNumberIn2DArray(
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 19)
    print(ret)
