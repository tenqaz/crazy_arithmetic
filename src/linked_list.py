"""
@author: Jim
@project: crazy_arithmetic
@file: linked_list.py
@time: 2019/12/1 15:25
@desc:

反转一个单链表
两两交换链表中的节点
判断链表是否有环
环形链表
"""


class ListNode(object):
    """
        链表节点
    """

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseList(self, head: ListNode) -> ListNode:
        """ 反转一个单链表

        Args:
            head (ListNode): 链表头结点

        Returns:
            返回反转后的头结点
        """

        last_node = None
        current_node = head
        while current_node:
            next_node = current_node.next

            current_node.next = last_node
            last_node = current_node

            current_node = next_node

        return last_node

    def swapPairs(self, head: ListNode):
        """ 两两交换链表中的节点

        给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
        你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

        输入: 1->2->3->4
        输出: 2->1->4->3

        :type head: ListNode
        :rtype: ListNode
        """

        pre = self
        pre.next = head

        while pre.next and pre.next.next:
            first_node = pre.next
            second_node = pre.next.next

            pre.next, second_node.next, first_node.next = second_node, first_node, second_node.next

            pre = first_node

        return self.next

    def hasCycle1(self, head: ListNode):
        """  判断链表是否有环：

        解法: 快慢指针

        :type head: ListNode
        :rtype: bool
        """

        fast = slow = head

        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return True

        return False

    def hasCycle2(self, head: ListNode):
        """  判断链表是否有环
        解法: 哈希表判重方式

        :type head: ListNode
        :rtype: bool
        """

        cache = set()
        while head:
            if head in cache:
                return True
            else:
                cache.add(head)
                head = head.next

        return False

    def detectCycle1(self, head: ListNode):
        """ 环形链表

        解法: 哈希表

        leetcode: 142

        :type head: ListNode
        :rtype: ListNode
        """

        cache = set()

        while head:
            if head in cache:
                return head

            cache.add(head)
            head = head.next

        return None

    def detectCycle2(self, head: ListNode):
        """ 环形链表

        解法: 快慢指针

        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head

        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return fast

        return None


def init_reverseList():
    """
    [1,2,3,4,5,None]
    """
    x1 = ListNode(1)
    x2 = ListNode(2)
    x3 = ListNode(3)
    x4 = ListNode(4)
    x5 = ListNode(5)

    x1.next = x2
    x2.next = x3
    x3.next = x4
    x4.next = x5
    x5.next = None

    return x1


def init_swapPairs():
    """
    [1,2,3,4,None]
    """
    x1 = ListNode(1)
    x2 = ListNode(2)
    x3 = ListNode(3)
    x4 = ListNode(4)

    x1.next = x2
    x2.next = x3
    x3.next = x4
    x4.next = None

    return x1


def init_hasCycle():
    x1 = ListNode(3)
    x2 = ListNode(2)
    x3 = ListNode(0)
    x4 = ListNode(-4)

    x1.next = x2
    x2.next = x3
    x3.next = x4
    x4.next = x2

    return x1


if __name__ == "__main__":
    solution = Solution()

    # 反转链表
    # head = init_reverseList()
    # node = solution.reverseList(head)

    # head = init_swapPairs()
    # node = solution.swapPairs(head)

    # while node:
    #     print(node.val)
    #     node = node.next

    # head = init_hasCycle()
    # isCycle = solution.hasCycle(head)
    # print(isCycle)

    # res = solution.detectCycle2(head)
    # print(res.val)
