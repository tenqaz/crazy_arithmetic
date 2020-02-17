# -*- coding: utf-8 -*-

"""
@author: Jim
@project: crazy_arithmetic
@time: 2019/12/5 10:02
@desc:

    反转一个单链表

    https://leetcode-cn.com/problems/reverse-linked-list/
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

    def reverseList(self, head: ListNode) -> ListNode:
        """ 反转一个单链表

            迭代

            时间复杂度: O(n)
            空间复杂度: O(1)
        Args:
            head (ListNode): 链表头结点

        Returns:
            返回反转后的头结点
        """
        last_node = None
        current_node = head
        while current_node:
            next_node = current_node.next

            current_node.next = last_node
            last_node = current_node

            current_node = next_node

        return last_node
