"""
@author: Jim
@project: crazy_arithmetic
@file: 015_三数之和.py
@time: 2019/12/10 11:31
@desc:

    有一种方式使用双指针形式:
    首先排序使用快排: O(nlogn)，然后遍历nums, 从遍历a的下一个开始用两个指针指向首端b和末端c
        当 a + b + c > 0，则末端C向左移动一步，然后继续比较
        当 a + b + c < 0. 则首端向右移动一步，然后继续比较
        当 a + b + c = 0. 则ok

"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """

            使用哈希表完成。类似于两数之和

            时间复杂度: O(n^2)
            空间复杂度: On(n)

        Args:
            nums:

        Returns:

        """

        if len(nums) < 3:
            return []

        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i - 1]:
                continue

            d = {}

            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 1
                else:
                    res.add((v, -v - x, x))
        return map(list, res)


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    rst = solution.threeSum2(nums)
    print(list(rst))
