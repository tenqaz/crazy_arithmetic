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
            动态规划

            dp[i] = dp[j] + 1
        Args:
            nums:

        Returns:

        """

        if not nums or len(nums) == 0: return 0

        dp = [1 for _ in nums]

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

if __name__ == '__main__':
    solution = Solution()
    # result = solution.lengthOfLIS([10,9,2,5,3,7,101,18])  # 4
    result = solution.lengthOfLIS([3,2,1])
    print(result)