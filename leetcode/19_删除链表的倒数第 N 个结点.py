"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
"""

from tools.linked_list_tools import *


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head = p = q = ListNode(-1, head)

        for i in range(n):
            q = q.next

        while q.next:
            p = p.next
            q = q.next

        p.next = p.next.next

        return head.next


if __name__ == '__main__':
    # 案例1  结果：[1,2,3,5]
    # head = [1, 2, 3, 4, 5]
    # n = 2

    # 案例2 结果: 空
    head = [1]
    n = 1

    linklist_head = make_linkedlist(head)

    ret_head = Solution().removeNthFromEnd(linklist_head, n)
    print_linkedlist(ret_head)
