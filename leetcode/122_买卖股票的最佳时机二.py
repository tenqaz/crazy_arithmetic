"""
@author: Jim
@project: crazy_arithmetic
@file: 122_买卖股票的最佳时机二.py
@time: 2020/1/16 22:47
@desc:  
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。


每天可以买和卖同时操作

"""

from typing import List


class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        """
        贪心算法
        1. 只要未买入，则买入
        2. 只要后一天的价格大于持有的价格，则卖出赚取差价。
        3. 如果是最后一天，如果持有，就算亏损也要卖出。
        Args:
            prices:

        Returns:

        """

        total = 0
        buy = -1
        for index, item in enumerate(prices):
            if buy == -1:  # 买
                if index != len(prices) - 1 and item < prices[index + 1]:
                    buy = item
            else:  # 卖
                if item > buy and (index == len(prices) - 1 or item > prices[index + 1]):
                    total += item - buy
                    buy = -1

        return total

    def maxProfit(self, prices: List[int]) -> int:
        """
        动态规划

        最大利润
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i][0] - prices[i])
        Args:
            prices:

        Returns:

        """

        if len(prices) < 2:
            return 0

        dp = [[0, 0] for _ in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i-1][0] - prices[i])

        return dp[-1][0]


if __name__ == '__main__':
    solution = Solution()
    result = solution.maxProfit([7,1,5,3,6,4])
    print(result)
