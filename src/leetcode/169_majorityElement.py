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

from collections import defaultdict, Counter

from typing import List


class Solution:
    def majorityElement(self, nums, lo=0, hi=None):
        """  分而治之. 这太难想到了。。

        """

        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)

    def majorityElement2(self, nums: List[int]) -> int:
        """ 这里使用了对nums进行计数获取其中最大的值。
        """

        data = defaultdict(int)

        max_count = 0
        max_data = 0

        for i in nums:
            data[i] += 1

            if data[i] > max_count:
                max_count = data[i]
                max_data = i

        return max_data

    def majorityElement3(self, nums: List[int]) -> int:
        """
        算法逻辑和上面的一样，只是使用了python中内置库Counter

        """
        c = Counter(nums)
        return c.most_common(1)[0][0]

    def majorityElement4(self, nums: List[int]) -> int:
        """ 先排序，再取中间的那个数，一定是众数

        时间复杂度:
        """
        nums.sort()

        return nums[len(nums) // 2]

    def majorityElement5(self, nums):
        """ 摩尔投票法。最优

        数字大于一半，只要不同的相互抵消，则剩下的肯定就是众数

        时间复杂度: O(n)
        空间复杂度: O(1)
        """

        cur_num = nums[0]
        cur_count = 1
        for num in nums[1:]:
            if cur_num == num:
                cur_count += 1
            elif cur_count == 0:
                cur_count += 1
                cur_num = num
            else:
                cur_count -= 1

        return cur_num


if __name__ == '__main__':
    solution = Solution()
    data = solution.majorityElement5([6, 5, 5])
    print(data)
