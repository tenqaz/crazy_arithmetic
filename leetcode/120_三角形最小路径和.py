"""
@author: Jim
@project: crazy_arithmetic
@file: 120_三角形最小路径和.py
@time: 2020/2/2 20:46
@desc:  
    https://leetcode-cn.com/problems/triangle/
"""

from typing import List


class Solution:
    def _gen2(self, i, j):
        if len(self.trigangle) == i:
            return 0

        return self.trigangle[i][j] + min(self._gen(i + 1, j), self._gen(i + 1, j + 1))

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        """
            递归的方法，将所有的节点都走一遍。

            时间复杂度: 2^n

            结果: 超时

            时间: O(n)
        Args:
            triangle:

        Returns:

        """

        self.trigangle = triangle

        return self._gen2(0, 0)

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        """
            动态规划. 自顶向下相加
            每一层保存当前的状态、大小
        Args:
            triangle:

        Returns:

        """

        if not triangle:
            return 0

        if len(triangle) == 1:
            return triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])

        return min(triangle[-1])

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        动态规划。 自底向上相加

        时间复杂度：O(n^2)
        空间复杂度: O(1)

        Args:
            triangle:

        Returns:

        """
        if not triangle:
            return 0

        if len(triangle) == 1:
            return triangle[0][0]

        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]


if __name__ == '__main__':
    solution = Solution()
    result = solution.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ])

    # result = solution.minimumTotal([[-1], [2, 3], [1, -1, -3]])
    print(result)
