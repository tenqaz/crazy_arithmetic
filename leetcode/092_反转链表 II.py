"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2022/12/18 18:29
@desc:
    https://leetcode.cn/problems/reverse-linked-list-ii/
"""

from typing import List, Optional

from tools.linked_list_tools import ListNode, make_linkedlist, print_linkedlist


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode(-1, head)
        cur = head
        while cur:
            next = cur.next
            cur.next = next.next
            next.next = ret.next
            ret.next = next

        return ret.next


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]

    head = make_linkedlist(data)
    ret = Solution().reverseList(head)
    print_linkedlist(ret)
