#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File: 剑指 Offer II 004. 只出现一次的数字 .py
@Time: 2022/12/17 12:34:45
@Author: Jim
@Contact: zhengwenfeng37@gmail.com
@Desc: 
    https://leetcode.cn/problems/WGki4K/

    主要是用hash表来实现
'''

from typing import List
from collections import Counter


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        """ 使用Counter计数

        """
        freq = Counter(nums)
        for num, count in freq.items():
            if count == 1:
                return num

    def singleNumber2(self, nums: List[int]) -> int:
        """ 使用两个set分别记录：已经访问过的，和可能是单个数字的。

        """
        visited = set()
        result = set()

        for i in nums:
            if i in visited:
                if i in result:
                    result.remove(i)
            else:
                visited.add(i)
                result.add(i)

        return result.pop()


if __name__ == '__main__':
    # result: 3
    # nums = [2, 2, 3, 2]

    # result: 500
    nums = [30000, 500, 100, 30000, 100, 30000, 100]

    ret = Solution().singleNumber(nums)
    print(ret)
