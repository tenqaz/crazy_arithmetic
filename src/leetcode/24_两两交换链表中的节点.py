2  # -*- coding: utf-8 -*-

"""
@author: Jim
@project: crazy_arithmetic
@time: 2019/12/5 10:11
@desc:

    两两交换链表中的节点
    
    https://leetcode-cn.com/problems/swap-nodes-in-pairs/

"""


class ListNode(object):
    """
        链表节点
    """

    def __init__(self, x):
        self.val = x
        self.next = None


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

    def swapPairs(self, head: ListNode):
        """ 两两交换链表中的节点

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


if __name__ == '__main__':
    head = make_linkedlist([1, 2, 3, 4])
    s = Solution()
    ret = s.swapPairs(head)
    print_linkedlist(ret)
