"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2024/2/19 16:19
@desc:
   https://leetcode.cn/problems/minimum-path-sum/description/

   使用dp来保存每一步的最优解，而每一步都是由从上往下走，或者从左往右走的最小和再加上当前的值。
"""
from typing import List


class Solution:

    def minPathSum2(self, grid: List[List[int]]) -> int:
        """
            这个是我写的自底向上的解法，想象一幅二叉树图，就是明白为什么是自底向上了。
            动态转移方程：

            当 i = 0 and j = 0时
                dp[0][0] = grid[0][0]
            当 i = 0 and j != 0时
                dp[i][j] = grid[i][j] + dp[i][j - 1]
            当 j = 0 and i != 0时
                dp[i][j] = grid[i][j] + dp[i - 1][j]
            当 i != 0 and j !=0时
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

            优化：
            在for循环中，包含的逻辑太多，可以挪到外部去做初始化。

        """

        grid_m = len(grid)
        grid_n = len(grid[0])

        dp = [[0] * grid_n] * grid_m
        dp[0][0] = grid[0][0]

        for i in range(grid_m):
            for j in range(grid_n):

                # 第一个不计算
                if i == 0 and j == 0:
                    continue

                # 第一行
                if i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                    continue

                # 第一列
                if j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                    continue

                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[grid_m - 1][grid_n - 1]

    def minPathSum3(self, grid: List[List[int]]) -> int:
        """
            对比minPathSum2进行了优化
        """
        grid_m = len(grid)
        grid_n = len(grid[0])

        dp = [[0] * grid_n for _ in range(grid_m)]
        dp[0][0] = grid[0][0]

        for i in range(1, grid_m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]

        for j in range(1, grid_n):
            dp[0][j] = grid[0][j] + dp[0][j - 1]

        for i in range(1, grid_m):
            for j in range(1, grid_n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[grid_m - 1][grid_n - 1]

    def minPathSum4(self, grid: List[List[int]]) -> int:
        """ 自顶向下 """

        m = len(grid)
        n = len(grid[0])

        def gen(i, j):

            if i == 0 and j == 0:
                return grid[0][0]

            if i < 0 or j < 0:
                return float('inf')

            return min(gen(i - 1, j), gen(i, j - 1)) + grid[i][j]

        return gen(m - 1, n - 1)

    def minPathSum(self, grid: List[List[int]]) -> int:
        """
            自顶向下

            在minPathSum4的基础上加上了缓存，通过剪枝，避免重复计算
        """

        m = len(grid)
        n = len(grid[0])

        cache = [[-1 for _ in range(m)] for _ in range(n)]

        def gen(i, j):

            if i == 0 and j == 0:
                return grid[0][0]

            if i < 0 or j < 0:
                return float('inf')

            if cache[i][j] != -1:
                return cache[i][j]

            cache[i][j] = min(gen(i - 1, j), gen(i, j - 1)) + grid[i][j]

            return cache[i][j]

        return gen(m - 1, n - 1)


if __name__ == '__main__':
    # 7
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

    ret = Solution().minPathSum(grid)
    print(ret)
