"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2022/12/16 15:54
@desc:
    https://leetcode.cn/problems/lMSNwu/

    给定两个 非空链表 l1和 l2 来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
    可以假设除了数字 0 之外，这两个数字都不会以零开头。

"""

from tools.linked_list_tools import ListNode, make_linkedlist, print_linkedlist


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_stack = []
        l2_stack = []
        pre = ListNode(-1)

        while l1:
            l1_stack.append(l1)
            l1 = l1.next

        while l2:
            l2_stack.append(l2)
            l2 = l2.next

        jinwei = 0
        while l1_stack or l2_stack or jinwei:
            l2_num = l1_num = 0
            if l1_stack:
                l1_num = l1_stack.pop().val
            if l2_stack:
                l2_num = l2_stack.pop().val

            node_num = l1_num + l2_num + jinwei
            jinwei = 0
            if node_num > 9:
                node_num = node_num % 10
                jinwei = 1

            next = pre.next
            pre.next = ListNode(node_num, next)

        if jinwei:
            next_node = pre.next
            pre.next = ListNode(1)
            pre.next.next = next_node

        return pre.next


if __name__ == "__main__":
    # [7, 8, 0, 7]
    l1 = [7, 2, 4, 3]
    l2 = [5, 6, 4]

    # [1, 0]
    # l1 = [5]
    # l2 = [5]
    head1 = make_linkedlist(l1)
    head2 = make_linkedlist(l2)

    ret = Solution().addTwoNumbers(head1, head2)
    print_linkedlist(ret)
