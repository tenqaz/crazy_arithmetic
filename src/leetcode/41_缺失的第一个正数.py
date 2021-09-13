"""
@author: Jim
@project: crazy_arithmetic
@file: 41_缺失的第一个正数.py
@time: 2021/6/6 12:23
@desc:  
    给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

    请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
"""

import heapq
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = heapq.nsmallest(len(nums), nums)

        num = 1

        for i in range(len(nums)):
            if nums[i] <= 0:
                continue

            if nums[i] != num:
                break



        return num


if __name__ == '__main__':
    s = Solution()
    # data = [1]  # 2
    # data = [1,2,0]  # 3
    # data = [3,4,-1,1]  # 2
    # data = [7,8,9,11,12]  # 1
    data = [0, 2, 2, 1, 1]
    ret = s.firstMissingPositive(data)
    print(ret)
