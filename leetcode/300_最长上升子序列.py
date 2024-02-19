"""
@author: Jim
@project: crazy_arithmetic
@file: 300_最长上升子序列.py
@time: 2020/2/8 20:45
@desc:  
    https://leetcode-cn.com/problems/longest-increasing-subsequence/

    [10,9,2,5,3,7,101,18]
"""

from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
            遍历两次，
            1. 外部循环式获取dp[i]可能性的最大值
            2. 内层循环， 遍历前面每一个dp的可能性，求出dp[i]的最大值
        """

        nums_len = len(nums)
        dp = [1] * nums_len

        for i in range(1, nums_len):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    result = solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])  # 4
    # result = solution.lengthOfLIS([3,2,1])
    print(result)
