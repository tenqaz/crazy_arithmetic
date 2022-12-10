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

        推导公式:
            dp[i][0] = max(dp[i-1][0]*a[i], dp[i-1][1]*a[i])
            dp[i][1] = min(dp[i-1][1]*a[i], dp[i-1][0]*a[i])

            0代表着最大值
            1代表着最小值，负负得正。
        """
        
        dp = [[0, 0] for i in range(len(nums))]
        
        res = dp[0][0] = dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
            dp[i][1] = min(dp[i-1][1]*nums[i], dp[i-1][0]*nums[i], nums[i])
            res = max(dp[i][0], res)
        
        return res

    def maxProduct2(self, nums: List[int]) -> int:
        """
            推导公式:
                dp[i][0] = max(dp[i-1][0]*a[i], dp[i-1][1]*a[i])
                dp[i][1] = min(dp[i-1][1]*a[i], dp[i-1][0]*a[i])

                0代表着最大值
                1代表着最小值，负负得正。

            在上面的动态规划中，再使用滚动数组进行优化，将空间复杂度改为O(1)
        """
    
        dp = [[0, 0] for i in range(2)]
        
        res = dp[0][0] = dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            x, y = i % 2, (i-1) % 2
            dp[x][0] = max(dp[y][0]*nums[i], dp[y][1]*nums[i], nums[i])
            dp[x][1] = min(dp[y][1]*nums[i], dp[y][0]*nums[i], nums[i])
            res = max(dp[x][0], res)
        
        return res
         

    def maxProduct3(self, nums: List[int]) -> int:
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