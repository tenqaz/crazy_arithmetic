#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File: 002_两数相加.py
@Time: 2022/12/14 17:50:34
@Author: Jim
@Contact: zhengwenfeng37@gmail.com
@Desc: 
    https://leetcode.cn/problems/add-two-numbers/
'''


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linkedlist(head: ListNode):
    print("--------分割线------")
    while head:
        print(head.val)
        head = head.next


def make_linkedlist(value_list):
    if not value_list:
        return

    head = ListNode(value_list[0])
    cur_node = head

    for i in value_list[1:]:
        node = ListNode(i)
        cur_node.next = node
        cur_node = node

    return head


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        current_node = ret_node = ListNode(-1)

        jinwei = 0
        while l1 or l2:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
            if l2:
                v2 = l2.val

            count = v1 + v2 + jinwei
            jinwei = 0

            if count > 9:
                count %= 10
                jinwei = 1

            current_node.next = ListNode(count)
            current_node = current_node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if jinwei:
            last_node = ListNode(1)
            current_node.next = last_node

        return ret_node.next


if __name__ == '__main__':
    # 输出 [7,0,8]
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]

    # 输出 [7,0,0,1]
    l1 = [2, 4, 3]
    l2 = [5, 6, 6]
    head1 = make_linkedlist(l1)
    head2 = make_linkedlist(l2)

    s = Solution()
    ret = s.addTwoNumbers(head1, head2)

    print_linkedlist(ret)