"""
    https://leetcode-cn.com/problems/middle-of-the-linked-list/

    给定一个头结点为 head 的非空单链表，返回链表的中间结点。

    如果有两个中间结点，则返回第二个中间结点。


思路：
    1. 快指针走两步，慢指针走一步
    2. 快指针走到终点后，慢指针就是中点。
    3. 中点可能是一个结点，也可能是两个。
"""

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


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        p = head
        q = head

        while q.next and q.next.next:
            p = p.next
            q = q.next.next

        if q.next is None:
            return p
        else:
            return p.next


if __name__ == '__main__':
    head = make_linkedlist([1,2,3,4,5,6])

    s = Solution()
    head = s.middleNode(head)
    print(head.val)

