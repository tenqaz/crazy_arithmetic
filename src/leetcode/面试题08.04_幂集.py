"""
@author: Jim
@project: crazy_arithmetic
@file: 面试题08.04_幂集.py
@time: 2021/5/29 17:17
@desc:  
    https://leetcode-cn.com/problems/power-set-lcci/

"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        result = []

        def dfs(x, tmp):
            result.append(tmp)
            for i in range(x, nums_len):
                dfs(i + 1, tmp + [nums[i]])

        dfs(0, [])

        return result


if __name__ == '__main__':
    s = Solution()
    r = s.subsets([1, 2, 3])
    print(r)
