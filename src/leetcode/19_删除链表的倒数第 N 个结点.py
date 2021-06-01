"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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