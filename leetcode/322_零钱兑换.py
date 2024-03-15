"""
@author: Jim
@project: crazy_arithmetic
@file: 322_零钱兑换.py
@time: 2020/2/11 19:02
@desc:  
    
"""

from typing import List


class Solution:

    def coinChange2(self, coins: List[int], amount: int) -> int:
        """ 暴力递推
        """

        if amount == 0:
            return 0

        if amount < 0:
            return -1

        res = float('inf')

        for coin in coins:
            count = self.coinChange(coins, amount - coin)
            if count == -1:
                continue

            res = min(res, count + 1)


    def coinChange3(self, coins: List[int], amount: int) -> int:
        """ 暴力递推，使用缓存，不用重复计算
        """

        cache = {}

        def gen(coins: List[int], amount: int) -> int:

            if amount == 0:
                return 0

            if amount < 0:
                return -1

            if amount in cache:
                return cache[amount]

            res = float('inf')

            for coin in coins:
                count = self.coinChange(coins, amount - coin)
                if count == -1:
                    continue

                res = min(res, count + 1)

            cache[amount] = res if res != float('inf') else -1
            return cache[amount]

        return gen(coins, amount)

    def coinChange(self, coins: List[int], amount: int) -> int:
        """ 使用dp的方式进行递推

        """

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue

                dp[i] = min(dp[i-coin] + 1, dp[i])

        return -1 if dp[amount] == amount + 1 else dp[amount]


if __name__ == '__main__':
    solution = Solution()
    result = solution.coinChange([1, 2, 5], 11)
    print(result)
