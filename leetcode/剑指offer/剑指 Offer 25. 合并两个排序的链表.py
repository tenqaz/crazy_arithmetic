"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/23 14:12
@desc:
    https://leetcode.cn/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/?envType=study-plan-v2&envId=coding-interviews
"""
from tools.linked_list_tools import make_linkedlist, print_linkedlist


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """递归"""

        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """  遍历链表 """
        pre_node = dummy_node = ListNode(-1)

        while l1 and l2:
            if l1.val < l2.val:
                pre_node.next = l1
                l1 = l1.next
            else:
                pre_node.next = l2
                l2 = l2.next

            pre_node = pre_node.next

        pre_node.next = l1 if l1 else l2

        return dummy_node.next


if __name__ == '__main__':
    l1 = make_linkedlist([1, 2, 4])
    l2 = make_linkedlist([1, 3, 4])
    s = Solution()
    ret_head = s.mergeTwoLists(l1, l2)
    print_linkedlist(ret_head)
