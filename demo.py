"""
    冒泡排序

    两两交换，将大的值往后放。
"""

from typing import List, Optional

from tools.linked_list_tools import ListNode, make_linkedlist, print_linkedlist


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        ret = p = ListNode(-1, head)

        for _ in range(left - 1):
            p = p.next

        cur = p.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = p.next
            p.next = next


        return ret.next


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    left = 2
    right = 4

    head = make_linkedlist(data)
    ret = Solution().reverseBetween(head, left, right)
    print_linkedlist(ret)
