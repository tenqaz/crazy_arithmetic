"""
@author: Jim
@project: crazy_arithmetic
@file: 26_删除排序数组中的重复项.py
@time: 2021/1/3 23:19
@desc:

    fast指针在前面探路，如果和slow不同，则将值赋给slow，slow再进行+1,。
    
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1

        nums_len = len(nums)
        while fast < nums_len:
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
ret = Solution().removeDuplicates(nums)
# 5, nums = [0,1,2,3,4]
print(ret)
print(nums)
