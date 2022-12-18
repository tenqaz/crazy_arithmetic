#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File: 剑指 Offer II 007. 数组中和为 0 的三个数.py
@Time: 2022/12/17 14:27:57
@Author: Jim
@Contact: zhengwenfeng37@gmail.com
@Desc: 
    暴力不考虑

    https://leetcode.cn/problems/1fGaJU/

    和leetcode15题相同
'''



from typing import List


class Solution:
    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        """排序+二分法"""
        pass

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        """排序+双指针"""
        pass

    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        """
            单重循环+哈希表

            未想到：
                需要考虑如何去重相同的结果，这里用的是先排序，遇到相同的数字则跳过
        """

        nums.sort()
        ret = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            cache_set = set()
            for j in nums[i + 1:]:
                target = - v - j
                if target in cache_set:
                    ret.add((v, target, j))
                else:
                    cache_set.add(j)

        return list(map(list, ret))


if __name__ == "__main__":
    # result: [[-1, 0, 1], [-1, -1, 2]]
    # nums = [-1, 0, 1, 2, -1, -4]

    # result: [0,0,0]
    nums = [0, 0, 0, 0]
    solution = Solution()
    rst = solution.threeSum(nums)
    print(rst)