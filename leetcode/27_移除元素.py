"""
@author: Jim
@project: crazy_arithmetic
@time: 2024-03-12
@desc:
    
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast, slow = 0, 0

        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        return slow


nums = [3, 2, 2, 3]
val = 3
ret = Solution().removeElement(nums, val)
print(ret)
