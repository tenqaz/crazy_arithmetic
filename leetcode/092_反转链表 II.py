"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2022/12/18 18:29
@desc:
    https://leetcode.cn/problems/reverse-linked-list-ii/
"""

from typing import List, Optional

from tools.linked_list_tools import ListNode, make_linkedlist, print_linkedlist


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode):

        last_node = None

        while head:
            next_node = head.next
            head.next = last_node
            last_node = head
            head = next_node

        return last_node

    def reverseBetween2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """ 通过截取指定范围内的链表，然后再将该链表反转，最后再接回原链表

        """

        dummy_node = ListNode(val=-1, next=head)
        pre = dummy_node

        for i in range(left - 1):
            pre = pre.next
        left_node = pre.next

        right_node = pre
        for i in range(right - left + 1):
            right_node = right_node.next

        succ_node = right_node.next

        # 截断中间链表
        pre.next = None
        right_node.next = None

        self.reverseList(left_node)

        # 恢复
        pre.next = right_node
        left_node.next = succ_node
        return dummy_node.next

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
            逐个置换
        """

        dummy_node = ListNode(-1, next=head)
        pre = dummy_node
        for i in range(left - 1):
            pre = pre.next

        cur_node = pre.next

        for i in range(right - left):
            next_node = cur_node.next
            cur_node.next = next_node.next
            next_node.next = pre.next
            pre.next = next_node

        return dummy_node.next


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]

    head = make_linkedlist(data)
    ret = Solution().reverseBetween(head, 2, 4)
    print_linkedlist(ret)
