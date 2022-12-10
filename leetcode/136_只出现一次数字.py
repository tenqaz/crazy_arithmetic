"""
@author: Jim
@project: crazy_arithmetic
@file: 136_只出现一次数字.py
@time: 2021/9/19 22:47
@desc:

https://leetcode-cn.com/problems/single-number/
    
"""

from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """ 位运算

            a^a=0；自己和自己异或等于0
            a^0=a；任何数字和0异或还等于他自己
            a^b^c=a^c^b；异或运算具有交换律
        """
        ret = 0
        for i in nums:
            ret ^= i

        return ret

    def singleNumber2(self, nums: List[int]) -> int:
        """ 位运算。 最优解

            思路和上面位运算一样，只是减少了ret变量，更加的简洁
        """
        return reduce(lambda x, y: x ^ y, nums)

    def singleNumber3(self, nums: List[int]) -> int:
        """ 先排序再遍历查询
        """
        nums = sorted(nums)
        nums_len = len(nums)
        for index in range(0, nums_len, 2):
            if index + 1 == nums_len or nums[index] != nums[index + 1]:
                return nums[index]

    def singleNumber3(self, nums: List[int]) -> int:
        """ 先排序再遍历查询
        """
        nums = sorted(nums)
        nums_len = len(nums)
        for index in range(0, nums_len, 2):
            if index + 1 == nums_len or nums[index] != nums[index + 1]:
                return nums[index]

    def singleNumber4(self, nums: List[int]) -> int:
        """ 使用set
        """

        nums_set = set()
        for num in nums:
            if num in nums_set:
                nums_set.remove(num)
            else:
                nums_set.add(num)

        return nums_set.pop()


s = Solution()
ret = s.singleNumber4([4, 1, 2, 1, 2])
print(ret)
