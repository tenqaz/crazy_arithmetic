"""

leetcode: https://leetcode-cn.com/problems/rotate-array/

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
"""

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums_len = len(nums)
        k %= nums_len
        self.reverse(nums, 0, nums_len-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, nums_len-1)

    def reverse(self, nums, start ,end):

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]

            start += 1
            end -= 1
