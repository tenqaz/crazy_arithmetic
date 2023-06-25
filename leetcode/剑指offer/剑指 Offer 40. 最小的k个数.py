"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/25 20:29
@desc:
    https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/?envType=study-plan-v2&envId=coding-interviews
"""
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]

