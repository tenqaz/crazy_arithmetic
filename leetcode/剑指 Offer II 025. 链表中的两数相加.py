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
        ret_head = cur_head = ListNode(-1)

        while l1:
            l1_stack.append(l1.val)
            l1 = l1.next

        while l2:
            l2_stack.append(l2.val)
            l2 = l2.next

        jinwei = 0
        while l1_stack or l2_stack or jinwei:
            l1_data = l2_data = 0

            if l1_stack:
                l1_data = l1_stack.pop()

            if l2_stack:
                l2_data = l2_stack.pop()

            data_sum = l1_data + l2_data + jinwei
            jinwei = 0

            if data_sum > 9:
                jinwei = 1
                data_sum %= 10

            last_node = ListNode(data_sum)
            if cur_head.next:
                next_node = cur_head.next
                cur_head.next = last_node
                last_node.next = next_node
            else:
                cur_head.next = last_node

        return ret_head.next


if __name__ == '__main__':
    l1 = [7, 2, 4, 3]
    l2 = [5, 6, 4]
    head1 = make_linkedlist(l1)
    head2 = make_linkedlist(l2)

    ret = Solution().addTwoNumbers(head1, head2)
    print_linkedlist(ret)
