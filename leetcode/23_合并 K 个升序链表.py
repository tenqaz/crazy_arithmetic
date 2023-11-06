import heapq
from typing import Optional, List

from arithmetic.tools.linked_list_tools import ListNode, make_linkedlist, print_linkedlist

ListNode.__lt__ = lambda self, other: self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """ 堆

        1. 将每个链表中的头结点入端中，构成一个大顶堆
        2. 创建一个虚拟节点
        3. 从大顶堆中取出最小值，并将其插入到虚拟节点的下一个节点中
        4. 然后其next节点再次放入到大顶堆中
        5. 重复3、4步骤，直至大顶堆为空
        6. 返回虚拟节点的下一个节点即为合并后的链表

        Args:
            lists:

        Returns:

        """

        pq = []
        dummy = cur = ListNode(-1)

        for head in lists:
            if head:
                heapq.heappush(pq, (head.val, head))

        while pq:
            item = heapq.heappop(pq)[1]

            cur.next = item
            cur = cur.next

            if item.next:
                heapq.heappush(pq, (item.next.val, item.next))

        return dummy.next


if __name__ == '__main__':
    # [
    #   1->4->5,
    #   1->3->4,
    #   2->6
    # ]
    lists = [make_linkedlist([1, 4, 5]), make_linkedlist([1, 3, 4]), make_linkedlist([2, 6])]

    print(print_linkedlist(Solution().mergeKLists(lists)))