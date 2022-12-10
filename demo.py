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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = slow = ListNode(-1, head)

        for i in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
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
