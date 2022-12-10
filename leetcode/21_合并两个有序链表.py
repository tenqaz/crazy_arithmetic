"""
    https://leetcode-cn.com/problems/merge-two-sorted-lists/

    将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
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

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        cur = head

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1

                l1 = l1.next
            else:
                cur.next = l2

                l2 = l2.next

            cur = cur.next

        if l1:
            cur.next = l1
        else:
            cur.next = l2

        return head.next


if __name__ == '__main__':
    head1 = make_linkedlist([1, 2, 4])
    head2 = make_linkedlist([1, 3, 4])

    s = Solution()
    head = s.mergeTwoLists(head1, head2)
    print_linkedlist(head)