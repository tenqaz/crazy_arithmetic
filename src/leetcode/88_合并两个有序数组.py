"""
@author: Jim
@project: crazy_arithmetic
@file: 88_合并两个有序数组.py
@time: 2021/9/20 14:45
@desc:  
    https://leetcode-cn.com/problems/merge-sorted-array/submissions/
"""

from typing import List


class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """ 先将nums2添加到nums1末尾，再排序

        时间复杂度: O(nlogn)
        空间复杂度: O(1)
        """
        pass

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """ 双指针，分别指向两个数组，比较大小放在一个新数组里，再用新数组放在nums中
            时间复杂度: O(m+n)
            空间复杂度：O(m+n)
        """
        pass

    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """ 双指针逆序放，不需要移动移动数组   推荐

            时间复杂度: O(n)
            空间复杂度 O(1)
        """

        p = m - 1
        q = n - 1
        nums1_last_index = m + n - 1

        while p >= 0 or q >= 0:
            if p == -1:
                nums1[nums1_last_index] = nums2[q]
                q -= 1
            elif q == -1:
                nums1[nums1_last_index] = nums1[p]
                p -= 1
            elif nums1[p] > nums2[q]:
                nums1[nums1_last_index] = nums1[p]
                p -= 1
            else:
                nums1[nums1_last_index] = nums2[q]
                q -= 1

            nums1_last_index -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

nums1 = [1]
m = 1
nums2 = []
n = 0

# [1]
nums1 = [0]
m = 0
nums2 = [1]
n = 1

s = Solution()
s.merge3(nums1, m, nums2, n)
print(nums1)
