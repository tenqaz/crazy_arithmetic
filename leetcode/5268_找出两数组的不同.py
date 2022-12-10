"""
@author: Jim
@project: crazy_arithmetic
@file: 5268_找出两数组的不同.py
@time: 2022/3/27 19:37
@desc:  

    使用Set类型，可以进行差集获取到结果。
"""
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums_set = set(nums1)
        nums2_set = set(nums2)

        rs1 = nums_set - nums2_set
        rs2 = nums2_set - nums_set

        return [list(rs1), list(rs2)]
