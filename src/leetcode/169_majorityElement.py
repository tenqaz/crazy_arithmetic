"""
@author: Jim
@project: crazy_arithmetic
@file: 169_majorityElement.py
@time: 2019/12/18 17:50
@desc:

    给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

    你可以假设数组是非空的，并且给定的数组总是存在多数元素。

    示例 1:
    输入: [3,2,3]
    输出: 3

    示例 2:
    输入: [2,2,1,1,1,2,2]
    输出: 2

    1. map
    2. 排序
    3. 分而治之

"""

from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        data = defaultdict(int)

        max_count = 0
        max_data = 0

        for i in nums:
            data[i] += 1

            if data[i] > max_count:
                max_count = data[i]
                max_data = i

        return max_data
    
if __name__ == '__main__':
    solution = Solution()
    data = solution.majorityElement([2,2,1,1,1,2,2])
    print(data)

