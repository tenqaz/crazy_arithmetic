# -*- coding: utf-8 -*-

"""
@author: Jim
@project: crazy_arithmetic
@time: 2019/12/4 17:06
@desc:
    设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

"""

from __future__ import annotations

import heapq
from typing import List


class KthLargest(object):
    """
        1. init 中建堆
        2. 插入的时候，如果满了，并且堆顶小于插入的元素，则

    """

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """

        self._k = k
        self._heap = [0]
        self._count = 0

        while nums:
            self.add(nums.pop())

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        # 如果堆满了
        if self._count == self._k:
            if val > self._heap[1]:  # 如果大于堆顶元素，则替换堆顶从上往下的堆化
                self._heap[1] = val

                self._sort_down()

            else:  # 如果小于等于堆顶元素，则不变
                pass

        else:  # 如果堆没满，则插入到尾部，并进行从下往上的堆化
            self._count += 1
            self._heap.append(val)
            self._sort_up()

        return self._heap[1]

    @classmethod
    def _parent(self, child_index: int) -> int:
        """
            通过子节点的索引推导出父节点的索引

            Args(int):
                child_index: 子节点的索引

            Returns(int):
                父节点的索引
        """
        return child_index // 2

    @classmethod
    def _left_child(self, parent_index: int) -> int:
        """
            通过父节点的索引得到左子节点索引

            Args:
                parent_index(int): 父节点索引

            Return:
                左子节点索引

        """

        return parent_index * 2

    @classmethod
    def _right_child(self, parent_index: int) -> int:
        """
            通过父节点的索引得到右子节点索引

            Args:
                parent_index(int): 父节点索引

            Return:
                右子节点索引

        """

        return parent_index * 2 + 1

    def _sort_down(self) -> None:
        """
            小顶锥, 从顶向下堆化.

            Args:
                pass
        """

        parent_index = smaller_child_index = 1

        while True:
            left_index, right_index = KthLargest._left_child(parent_index), KthLargest._right_child(parent_index)

            if left_index <= self._count and self._heap[left_index] < self._heap[smaller_child_index]:
                smaller_child_index = left_index
            if right_index <= self._count and self._heap[right_index] < self._heap[smaller_child_index]:
                smaller_child_index = right_index

            if smaller_child_index == parent_index:
                break

            self._heap[smaller_child_index], self._heap[parent_index] = self._heap[parent_index], self._heap[
                smaller_child_index]
            parent_index = smaller_child_index

    def _sort_up(self) -> None:
        """
            小顶锥, 从下往上堆化

            Args:
                pass
        """

        current_index = self._count
        parent_index = KthLargest._parent(current_index)

        while parent_index and self._heap[current_index] < self._heap[parent_index]:
            self._heap[current_index], self._heap[parent_index] = self._heap[parent_index], self._heap[current_index]
            current_index, parent_index = parent_index, KthLargest._parent(parent_index)

    # *******  使用内置库实现  *******
    def __init__2(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k

        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add2(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]

if __name__ == "__main__":
    # kthLargest = KthLargest(2, [0])
    kthLargest = KthLargest(3, [4, 5, 8, 2])

    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(10))
    print(kthLargest.add(9))
    print(kthLargest.add(4))
