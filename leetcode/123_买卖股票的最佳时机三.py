"""
@author: Jim
@project: crazy_arithmetic
@file: 123_买卖股票的最佳时机三.py
@time: 2020/2/8 19:23
@desc:  
    https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/
"""

from typing import List


class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        """
         动态规划。 未解出

         dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])  # 空
         dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k][1] - prices[i])  # 买
         i: 天数
         j: 0空，1已买
         k: 2次数

         6
        Args:
            prices:

        Returns:

        """

        max_k = 2
        prices_len = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(2)] for i in range(prices_len)]

        for i in range(prices_len):
            for k in range(max_k):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])  # 空
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k][1] - prices[i])  # 买

        print(dp)
        return dp[prices_len - 1][max_k - 1][0]

    def maxProfit(self, prices):
        if prices == []:
            return 0
        length = len(prices)
        # 结束时的最高利润=[天数][是否持有股票][卖出次数]
        dp = [[[0, 0, 0], [0, 0, 0]] for i in range(0, length)]
        # 第一天休息
        dp[0][0][0] = 0
        # 第一天买入
        dp[0][1][0] = -prices[0]
        # 第一天不可能已经有卖出
        dp[0][0][1] = float('-inf')
        dp[0][0][2] = float('-inf')
        # 第一天不可能已经卖出
        dp[0][1][1] = float('-inf')
        dp[0][1][2] = float('-inf')
        for i in range(1, length):
            # 未持股，未卖出过，说明从未进行过买卖
            dp[i][0][0] = 0
            # 未持股，卖出过1次，可能是今天卖的，可能是之前卖的
            dp[i][0][1] = max(dp[i - 1][1][0] + prices[i], dp[i - 1][0][1])
            # 未持股，卖出过2次，可能是今天卖的，可能是之前卖的
            dp[i][0][2] = max(dp[i - 1][1][1] + prices[i], dp[i - 1][0][2])
            # 持股，未卖出过，可能是今天买的，可能是之前买的
            dp[i][1][0] = max(dp[i - 1][0][0] - prices[i], dp[i - 1][1][0])
            # 持股，卖出过1次，可能是今天买的，可能是之前买的
            dp[i][1][1] = max(dp[i - 1][0][1] - prices[i], dp[i - 1][1][1])
            # 持股，卖出过2次，不可能
            dp[i][1][2] = float('-inf')
        return max(dp[length - 1][0][1], dp[length - 1][0][2], 0)


if __name__ == '__main__':
    solution = Solution()
    result = solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
    print(result)
