2# -*- coding: utf-8 -*-

"""
@author: Jim
@project: crazy_arithmetic
@time: 2019/12/5 10:11
@desc:

    两两交换链表中的节点

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

    def swapPairs(self, head: ListNode):
        """ 两两交换链表中的节点

        给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
        你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

        输入: 1->2->3->4
        输出: 2->1->4->3

        :type head: ListNode
        :rtype: ListNode
        """

        pre = self  # 可以创建一个新的节点
        pre.next = head

        while pre.next and pre.next.next:
            first_node = pre.next
            second_node = pre.next.next

            pre.next, second_node.next, first_node.next = second_node, first_node, second_node.next

            pre = first_node

        return self.next
