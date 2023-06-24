"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/23 0:39
@desc:
    
"""
from typing import List

from tools.linked_list_tools import make_linkedlist


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint2(self, head: ListNode) -> List[int]:
        ret = []
        while head:
            ret.insert(0, head.val)
            head = head.next

        return ret

    def reversePrint(self, head: ListNode) -> List[int]:
        """ 递归 """
        return self.reversePrint(head.next) + [head.val] if head else []


if __name__ == '__main__':
    head = make_linkedlist([1, 3, 2])
    s = Solution()
    ret = s.reversePrint(head)
    print(ret)
