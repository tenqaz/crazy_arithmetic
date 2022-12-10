"""
@author: Jim
@project: crazy_arithmetic
@file: 322_零钱兑换.py
@time: 2020/2/11 19:02
@desc:  
    
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
            动态规划

            dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        Args:
            coins:
            amount:

        Returns:

        """

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == float('inf') else dp[amount]


if __name__ == '__main__':
    solution = Solution()
    result = solution.coinChange([1, 2, 5], 11)
    print(result)
