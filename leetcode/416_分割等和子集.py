"""
https://leetcode.cn/problems/partition-equal-subset-sum/description/
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """ 
            转换成背包问题 

            dp[i][j]
        """
        
        nums_len = len(nums)
        nums_sum = sum(nums)
        nums_half = nums_sum / 2

        dp = [[False for _ in range(nums_len)] for _ in range(nums_half)]

        

