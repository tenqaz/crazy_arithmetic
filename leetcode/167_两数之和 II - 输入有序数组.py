"""
    https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/

    在数组的两边分别设定一个指针，然后往中间移动，对两个指针的值进行相加,比较target:
    1. 如果两数之和大于target，右边的指针往左移，减少两数之和的大小。
    2. 如果两数之和小于target，左边的指针往右移，增加两数之和的大小。
    3. 相等则返回。
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) -1

        while left <= right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]