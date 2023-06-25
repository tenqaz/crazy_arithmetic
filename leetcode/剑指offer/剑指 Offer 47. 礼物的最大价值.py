"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/25 22:08
@desc:
    https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/?envType=study-plan-v2&envId=coding-interviews
"""
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])



