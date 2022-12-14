class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
            动态规划:

            当i>0,j=0时: dp[i][0] = dp[i-1][0] + grid[i][0]
            当i>0,j>0时: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            当i=0,j>0时: dp[0][j] = dp[0][j-1] + grid[0][j]

        Args:
            grid:

        Returns:

        """

        rows = len(grid)
        colums = len(grid[0])

        dp = [[0] * colums for i in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in range(1, colums):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, rows):
            for j in range(1, colums):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][colums - 1]


if __name__ == '__main__':
    data = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

    s = Solution()
    ret = s.minPathSum(data)
    print(ret)  # 7