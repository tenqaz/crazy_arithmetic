"""
@author: Jim
@project: crazy_arithmetic
@file: 121_买卖股票的最佳时机.py
@time: 2020/2/8 16:06
@desc:  
    
"""

from typing import List


class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        """
            暴利破解

            超出时间限制
        Args:
            prices:

        Returns:

        """

        max_value = 0

        for index, i in enumerate(prices):
            for j in prices[index + 1:]:
                if j - i > max_value:
                    max_value = j - i

        return max_value

    def maxProfit3(self, prices: List[int]) -> int:
        """
            第二种暴力
        Args:
            prices:

        Returns:

        """
        if len(prices) < 2:
            return 0

        min_value = prices[0]
        res = 0
        for i in prices[1:]:
            if i < min_value:
                min_value = i
                continue

            if i - min_value > res:
                res = i - min_value

        return res

    def maxProfit(self, prices: List[int]) -> int:
        """
            动态规划

            最大利润 = max{上一个最大利润, 当前值-最小值}
        Args:
            prices:

        Returns:

        """
        if len(prices) < 2:
            return 0

        max_value, min_value = 0, prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            min_value = min(min_value, price)
            max_value = max(max_value, price-min_value)

        return max_value



if __name__ == '__main__':
    solution = Solution()
    result = solution.maxProfit([7,1,5,3,6,4])
    print(result)