"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/25 19:44
@desc:
    
"""
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        count = 0
        for i, start in enumerate(nums):
            for j, item in enumerate(nums[i+1:]):
                if start > item:
                    count += 1

        return count

if __name__ == '__main__':
    print(Solution().reversePairs([7,5, 6, 4]))