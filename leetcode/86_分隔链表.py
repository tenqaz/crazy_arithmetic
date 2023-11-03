from typing import Optional

from arithmetic.tools.linked_list_tools import ListNode, make_linkedlist, print_linkedlist


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
            1. 首先创建两个虚拟头结点，分别用来保存小于x的节点和大于等于x的节点
            2. 然后再将两个链表进行合并
        """
        dummy_less_than = l1 = ListNode(-1)
        dummy_more_than = l2 = ListNode(-1)

        while head:

            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next

            next_node = head.next
            head.next = None
            head = next_node

        l1.next = dummy_more_than.next

        return dummy_less_than.next


if __name__ == '__main__':
    # output: [1,2,2,4,3,5]
    head = make_linkedlist([1, 4, 3, 2, 5, 2])
    x = 3

    # output: [1, 2]
    # head = make_linkedlist([2, 1])
    # x = 2
    print(print_linkedlist(Solution().partition(head, x)))