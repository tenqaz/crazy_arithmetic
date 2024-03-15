"""
    https://leetcode.cn/problems/maximum-subarray/description/
"""

from typing import List


class Solution:
    def maxSubArray2(self, nums: List[int]) -> int:
        """
            时间复杂度: O(n)
            空间复杂度: O(n)
        """
        
        nums_len = len(nums)
        dp = [0 for _ in range(nums_len)]
        dp[0] = nums[0]

        for i in range(1, nums_len):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        
        return max(dp)


    def maxSubArray(self, nums: List[int]) -> int:
        """
            在 maxSubArray2 的基础上优化空间。dp[i]只与dp[i-1]有关，所以不需要使用数组。
        
            时间复杂度: O(n)
            空间复杂度: O(1)
        """
        
        nums_len = len(nums)
        pre = nums[0]
        cur = 0
        res = pre

        for i in range(1, nums_len):
            cur = max(nums[i], pre + nums[i])
            pre = cur
            res = max(res, cur)
        
        return res

if __name__ == '__main__':
    # 6
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    
    # 1
    nums = [-2,1]
    ret = Solution().maxSubArray(nums)
    print(ret)