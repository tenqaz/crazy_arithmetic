"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/23 0:48
@desc:
    
"""
from tools.linked_list_tools import make_linkedlist, print_linkedlist


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last_node = None
        while head:
            next_node = head.next
            head.next = last_node
            last_node = head
            head = next_node

        return last_node


if __name__ == '__main__':
    head = make_linkedlist([1, 2, 3, 4, 5])
    s = Solution()
    ret = s.reverseList(head)
    print_linkedlist(ret)
