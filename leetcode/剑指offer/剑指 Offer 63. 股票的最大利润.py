"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/7/16 10:05
@desc:
    
"""
from typing import List
from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            每次循环，将当前值与前面的最小值相减取得到当前最大的利润值，然后和前面的最大利润值去最大值。
            再获取当前最小值。

            时间复杂度： O（n）
            控件复杂度： O（1）
        Args:
            prices:

        Returns:

        """
        max_profit = 0
        min_price = inf
        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)

        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
