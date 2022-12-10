    # -*- coding: utf-8 -*-

"""
@author: Jim
@project: crazy_arithmetic
@time: 2019/12/5 10:22
@desc:
    判断链表是否有环
    
    https://leetcode-cn.com/problems/linked-list-cycle/submissions/
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

    def hasCycle1(self, head: ListNode):
        """  判断链表是否有环：

        解法: 快慢指针

        :type head: ListNode
        :rtype: bool
        """

        fast = slow = head

        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return True

        return False

    def hasCycle2(self, head: ListNode):
        """  判断链表是否有环
        解法: 哈希表判重方式

        时间复杂度： O(n)
        空间复杂度: O(n)

        :type head: ListNode
        :rtype: bool
        """

        cache = set()
        while head:
            if head in cache:
                return True
            else:
                cache.add(head)
                head = head.next

        return False
