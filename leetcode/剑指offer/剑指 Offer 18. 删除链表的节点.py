"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/23 12:53
@desc:
    https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof/?envType=study-plan-v2&envId=coding-interviews
"""
from tools.linked_list_tools import make_linkedlist, print_linkedlist


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode2(self, head: ListNode, val: int) -> ListNode:
        """ 使用了虚拟头节点，因为匹配的值可能是第一个。 """

        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre_node = dummy_node
        cur_node = dummy_node.next
        while cur_node:
            if cur_node.val == val:
                pre_node.next = cur_node.next
                break

            pre_node = cur_node
            cur_node = cur_node.next

        return dummy_node.next

    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        """ 如果匹配的值是第一个直接返回即可. """
        if head.val == val: return head.next

        pre_node = head
        cur_node = head.next
        while cur_node:
            if cur_node.val == val:
                pre_node.next = cur_node.next
                break

            pre_node = cur_node
            cur_node = cur_node.next

        return head


if __name__ == '__main__':
    head = make_linkedlist([4, 5, 1, 9])
    s = Solution()
    ret_head = s.deleteNode(head, 5)
    print_linkedlist(ret_head)
