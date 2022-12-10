"""
@author: Jim
@project: crazy_arithmetic
@file: 704_二分查找.py
@time: 2021/9/20 12:50
@desc:  
    https://leetcode-cn.com/problems/binary-search/submissions/
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)-1

        while left <= right:
            mid = (right-left) // 2 + left

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1




# target = 4
nums = [-1,0,3,5,9,12]
target = 9


nums = [-1,0,3,5,9,12]
target = 13

# 1
nums = [1,4,7,11,15]
target = 4


s = Solution()
ret = s.search(nums, target)
print(ret)