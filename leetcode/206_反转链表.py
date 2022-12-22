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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linkedlist(head: ListNode):
    print("--------分割线------")
    while head:
        print(head.val)
        head = head.next


def make_linkedlist(value_list, none=None):
    if not value_list:
        return none

    head = ListNode(value_list[0])
    cur_node = head

    for i in value_list[1:]:
        node = ListNode(i)
        cur_node.next = node
        cur_node = node

    return head


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


if __name__ == '__main__':
    head = make_linkedlist([1, 2, 3, 4, 5])
    s = Solution()
    ret = s.reverseList(head)
    print_linkedlist(ret)
