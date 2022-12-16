"""
    冒泡排序

    两两交换，将大的值往后放。
"""

from typing import List, Optional

from tools.linked_list_tools import ListNode, make_linkedlist, print_linkedlist


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p = q = pre = ListNode(-1, head)

        for _ in range(left - 1):
            p = p.next

        while pre.next and pre.next and left < right:
            next_node = pre.next.next
            pre.next = next_node
            next_node.next



if __name__ == '__main__':
    pass
