"""
@author: Jim
@project: crazy_arithmetic
@file: 35_搜索插入位置.py
@time: 2021/9/20 16:20
@desc:  
    https://leetcode-cn.com/problems/search-insert-position/
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        while left <= right:

            mid = (right - left) // 2 + left
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid

        return left


# nums = [1,3,5,6]
# target = 5

# 1
nums = [1, 3, 5, 6]
target = 2

s = Solution()
ret = s.searchInsert(nums, target)
print(ret)


