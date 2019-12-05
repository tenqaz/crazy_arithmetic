# -*- coding: utf-8 -*-

"""
@author: Jim
@project: crazy_arithmetic
@time: 2019/12/5 10:23
@desc:

    获取探测环相交节点
"""

from __future__ import annotations

class ListNode(object):
    """
        链表节点
    """

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):



    def detectCycle1(self, head: ListNode):
        """ 环形链表

        解法: 哈希表

        leetcode: 142

        :type head: ListNode
        :rtype: ListNode
        """

        cache = set()

        while head:
            if head in cache:
                return head

            cache.add(head)
            head = head.next

        return None

    def detectCycle2(self, head: ListNode):
        """ 环形链表

        解法: 快慢指针

        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head

        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return fast

        return None