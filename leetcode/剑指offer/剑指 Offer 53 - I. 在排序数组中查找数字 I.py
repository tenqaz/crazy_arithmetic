"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/24 0:09
@desc:
    
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ret_count = 0
        for num in nums:
            if num == target:
                ret_count += 1

        return ret_count


