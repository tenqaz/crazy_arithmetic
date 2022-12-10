"""
@author: Jim
@project: crazy_arithmetic
@file: 26_删除排序数组中的重复项.py
@time: 2021/1/3 23:19
@desc:

给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

    
"""

from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:

        nums_len = len(nums)

        if nums_len < 2:
            return nums_len

        max_len = 1
        for index in range(1, nums_len):
            if nums[index] == nums[index - 1]:
                continue

            nums[max_len] = nums[index]
            max_len += 1

        return max_len
