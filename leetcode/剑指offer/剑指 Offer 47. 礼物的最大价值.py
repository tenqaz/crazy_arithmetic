"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/25 22:08
@desc:
    https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/?envType=study-plan-v2&envId=coding-interviews
"""
from typing import List


class Solution:
    def maxValue2(self, grid: List[List[int]]) -> int:
        """
            递归逆推，超时.

            可以优化，加上剪枝

        """

        def dfs(n, m):
            if n < 0 or m < 0:
                return 0

            return max(dfs(n - 1, m), dfs(n, m - 1)) + grid[n][m]

        row = len(grid) - 1
        column = len(grid[0]) - 1
        return dfs(row, column)

    def maxValue(self, grid: List[List[int]]) -> int:
        """
            动态规划。
            使用一个二维数组DP，计算每一个格子中的最大值，最后取最后一个格子中的值。
        Args:
            grid:

        Returns:

        """
        row = len(grid)
        column = len(grid[0])

        dp = [[0] * column for i in range(row)]

        for i in range(row):
            for j in range(column):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = max(dp[i][j - 1] + grid[i][j], dp[i][j])
                elif j == 0:
                    dp[i][j] = max(dp[i - 1][j] + grid[i][j], dp[i][j])
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

        return dp[row - 1][column - 1]


if __name__ == '__main__':
    # 12
    print(Solution().maxValue([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))

