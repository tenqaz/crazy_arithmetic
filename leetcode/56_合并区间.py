"""
@author: Jim
@project: crazy_arithmetic
@file: 56_合并区间.py
@time: 2021/9/20 16:46
@desc:  
    https://leetcode-cn.com/problems/merge-intervals/
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """ 先排序，再合并
        """
        intervals.sort()
        ret = []
        for index, record in enumerate(intervals):
            if not ret or record[0] > ret[-1][1]:
                ret.append(record)
            else:
                ret[-1][1] = max(ret[-1][1], record[1])

        return ret


# [[1,4]]
data = [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]

s = Solution()
ret = s.merge(data)
print(ret)

