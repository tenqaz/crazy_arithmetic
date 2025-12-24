# -*- coding: utf-8 -*-

"""
@author: Jim
@project: crazy_arithmetic
@time: 2019/12/9 18:09
@desc:

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
    给定 nums = [2, 7, 11, 15], target = 9

    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]

"""

from __future__ import annotations

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """

            通过遍历循环的方式计算和.
            时间复杂度: O(n^2)   不推荐


        Args:
            nums:
            target:

        Returns:

        """

        for index_i, i in enumerate(nums):
            for index_j, j in enumerate(nums[index_i + 1:]):
                if i + j == target:
                    return index_i, index_j + index_i + 1

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """

            利用hash表.

            时间复杂度 O(n)

        Args:
            nums:
            target:

        Returns:

        """

        cache = {}
        for index, record in enumerate(nums):
            if record in cache:
                return [cache[record], index]
            else:
                cache[target - record] = index


if __name__ == '__main__':
    # [0,1]
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    res = solution.twoSum2(nums, target)
    print(res)
