"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/23 15:50
@desc:
    https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/
"""
from typing import List


class Solution:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """
            哈希表

            时间复杂度: O(n)
            空间复杂度: O(n)
        """

        cache_set = set()
        for num in nums:
            if num in cache_set:
                return [num, target - num]

            cache_set.add(target - num)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            双指针，从左右两端往中间移动

            时间复杂度: O(n)
            空间福再度: O(1)
        """

        left, right = 0, len(nums) - 1

        while left < right:
            s = nums[left] + nums[right]
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                return [nums[left], nums[right]]

        return []


if __name__ == '__main__':
    s = Solution()
    ret = s.twoSum([14, 15, 16, 22, 53, 60], 76)
    print(ret)
