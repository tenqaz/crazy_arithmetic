#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File: 剑指 Offer II 008. 和大于等于 target 的最短子数组.py
@Time: 2022/12/20 21:09:22
@Author: Jim
@Contact: zhengwenfeng37@gmail.com
@Desc:
    https://leetcode.cn/problems/2VG8Kg/

"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        right = left = 0
        total = 0
        ans = len(nums) + 1

        while right < len(nums):

            total += nums[right]

            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1

            right += 1

        return 0 if ans == len(nums) + 1 else ans


if __name__ == "__main__":
    # 2
    # target = 7
    # nums = [2, 3, 1, 2, 4, 3]

    # 5
    target = 15
    nums = [1, 2, 3, 4, 5]

    print(Solution().minSubArrayLen(target, nums))
