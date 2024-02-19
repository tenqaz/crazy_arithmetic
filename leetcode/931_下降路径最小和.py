"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2024/2/19 17:56
@desc:

    https://leetcode.cn/problems/minimum-falling-path-sum/description/
    
"""
from typing import List


class Solution:
    def minFallingPathSum2(self, matrix: List[List[int]]) -> int:
        """
            自顶向下
        """

        matrix_len = len(matrix)

        dp = [[float('inf') for _ in range(matrix_len)] for _ in range(matrix_len)]

        for j in range(matrix_len):
            dp[0][j] = matrix[0][j]

        for i in range(1, matrix_len):
            for j in range(matrix_len):
                tmp = []
                tmp.append(dp[i - 1][j])

                if j - 1 >= 0:
                    tmp.append(dp[i - 1][j - 1])

                if j + 1 < matrix_len:
                    tmp.append(dp[i - 1][j + 1])

                dp[i][j] = min(tmp) + matrix[i][j]

        return min(dp[matrix_len - 1])

    def minFallingPathSum3(self, matrix: List[List[int]]) -> int:
        """
            自底向上
        """

        matrix_len = len(matrix)

        def gen(i, j):

            if i < 0 or j > matrix_len - 1 or j < 0:
                return float('inf')

            if i == 0:
                return matrix[i][j]

            return min(gen(i - 1, j), gen(i - 1, j - 1), gen(i - 1, j + 1)) + matrix[i][j]

        res = float('inf')
        for i in range(matrix_len):
            res = min(res, gen(matrix_len - 1, i))

        return res

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
            自底向上。
            在 minFallingPathSum3 的基础上进行缓存剪枝。
        """

        matrix_len = len(matrix)
        cache = [[float('inf') for _ in range(matrix_len)] for _ in range(matrix_len)]

        def gen(i, j):

            if i < 0 or j > matrix_len - 1 or j < 0:
                return float('inf')

            if i == 0:
                return matrix[i][j]

            if cache[i][j] != float('inf'):
                return cache[i][j]

            cache[i][j] = min(gen(i - 1, j), gen(i - 1, j - 1), gen(i - 1, j + 1)) + matrix[i][j]
            return cache[i][j]

        res = float('inf')
        for i in range(matrix_len):
            res = min(res, gen(matrix_len - 1, i))

        return res


if __name__ == '__main__':
    # 13
    matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    ret = Solution().minFallingPathSum(matrix)
    print(ret)
