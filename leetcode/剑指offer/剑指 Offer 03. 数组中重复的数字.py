"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/23 23:02
@desc:
    https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/?envType=study-plan-v2&envId=coding-interviews
"""
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        """
            哈希表

            时间复杂度：O(n)
            空间复杂度：O(n)

        """
        cache_set = set()
        for num in nums:
            if num in cache_set:
                return num

            cache_set.add(num)


if __name__ == '__main__':
    s = Solution()
    ret = s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3])
    print(ret)
