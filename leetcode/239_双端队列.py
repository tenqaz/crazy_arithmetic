# -*- coding: utf-8 -*-

"""
@author: Jim
@project: crazy_arithmetic
@time: 2019/12/9 15:25
@desc:

    给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

    返回滑动窗口中的最大值。
"""

from __future__ import annotations

from typing import List


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
            使用大根堆
        """
        pass

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        """

            使用双端队列的方式实现

            最左边保留最大的值.

            1. 在什么时候删除左边节点
            2. 在什么时候保留最大节点在最左边

        Args:
            nums(List[int]):
            k(int):

        Returns(List[int]):

        """
        if not nums: return []

        windows, res = [], []

        for i, x in enumerate(nums):
            if i >= k and windows[0] <= i - k:
                windows.pop(0)
            while windows and nums[windows[-1]] <= x:
                windows.pop()
            windows.append(i)

            if i >= k - 1:
                res.append(nums[windows[0]])

        return res


if __name__ == '__main__':
    # data = [1, 3, -1, -3, 5, 3, 6, 7]
    data = [1, 3, 1, 2, 0, 5]
    solution = Solution()
    res = solution.maxSlidingWindow(data, 3)
    print(res)
