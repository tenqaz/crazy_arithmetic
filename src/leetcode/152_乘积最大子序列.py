"""
@author: Jim
@project: crazy_arithmetic
@file: 152_乘积最大子序列.py
@time: 2020/2/7 18:32
@desc:  
    https://leetcode-cn.com/problems/maximum-product-subarray/
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """

            动态规划

        Args:
            nums:

        Returns:

        """

        res, cur_max, cur_min = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            cur_max, cur_min = cur_max * num, cur_min * num
            cur_max, cur_min = max(cur_max, cur_min, num), min(cur_max, cur_min, num)
            res = max(res, cur_max)

        return res

if __name__ == '__main__':
    solution = Solution()
    result = solution.maxProduct([2,3,-2,4])
    print(result)