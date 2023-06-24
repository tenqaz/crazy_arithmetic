"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/24 12:18
@desc:
    
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
            直接遍历

            时间复杂度：O(n)
            空间复杂度：O(1)
        """

        target = 0
        for num in nums:
            if num != target:
                return target

            target += 1

        return target


if __name__ == '__main__':
    s = Solution()
    ret = s.missingNumber([0])
    print(ret)
