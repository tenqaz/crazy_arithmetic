"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/23 14:06
@desc:
    https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
"""
from tools.linked_list_tools import make_linkedlist, print_linkedlist


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:

        p = q = head

        for i in range(k):
            q = q.next

        while q:
            q = q.next
            p = p.next

        return p


if __name__ == '__main__':
    head = make_linkedlist([1, 2, 3, 4, 5])
    s = Solution()
    ret_head = s.getKthFromEnd(head, 2)
    print_linkedlist(ret_head)
