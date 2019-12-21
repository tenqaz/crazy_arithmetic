"""
@author: Jim
@project: crazy_arithmetic
@file: 015_threeSum.py
@time: 2019/12/10 11:31
@desc:
    三个

"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """

            使用哈希表完成，标准答案.

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

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        """ 自己完成的算法. 还待完成.

        Args:
            nums:

        Returns:

        """

        nums.sort()
        res = set()

        for index, value in enumerate(nums[:-2]):

            tmp_data = set()

            for item in nums[index + 1:]:

                if -value - item not in tmp_data:
                    tmp_data.add(item)
                else:
                    res.add((value, item, -value - item))

        return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    rst = solution.threeSum2(nums)
    print(list(rst))
