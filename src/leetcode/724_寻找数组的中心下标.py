"""
@author: Jim
@project: crazy_arithmetic
@file: 724_寻找数组的中心下标.py
@time: 2021/9/20 15:53
@desc:  
    https://leetcode-cn.com/problems/find-pivot-index/


    SyntaxError: invalid syntax
               ^
    nums_len =
Line 5  (Solution.py)
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """ 先求和，再遍历，获取右边的值，再判断是否等于左边的值

            时间复杂度: O(n)
            空间复杂度: O(1)
        """
        nums_sum = sum(nums)

        left_sum = 0
        for i, num in enumerate(nums):
            if nums_sum - num - left_sum == left_sum:
                return i

            left_sum += num

        return -1
