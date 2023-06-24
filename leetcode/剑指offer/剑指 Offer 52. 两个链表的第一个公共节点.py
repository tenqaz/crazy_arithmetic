"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/23 14:48
@desc:
    https://leetcode.cn/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
"""
from tools.linked_list_tools import make_linkedlist, print_linkedlist


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
            哈希表
            时间复杂度: O(n)
            空间复杂度: O(n)
        """

        cache_node = set()

        while headA:
            cache_node.add(headA)
            headA = headA.next

        while headB:
            if headB in cache_node:
                return headB

            headB = headB.next

        return

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
            双指针

            时间复杂度：O(n)
            空间福再度：O(1)

            设：
            headA节点长度为m，需要a个节点达到公共节点
            headB节点长度n，需要b个节点达到公共节点
            公共节点长度为c

            创建两个指针pA和pB分别指向headA和headB的头节点
            a+c=m
            b+c=m
            如果a==b则两个指针会同时达到公共节点

            但如果a!=b,pA遍历完headA链表，在移动到headB链表的头部，pB遍历完headB链表，再移动到headA链表的头部。然后pA和pB继续移动，则会同时到达公共节点。
            pA移动了a+c+b次
            pB移动了b+c+a次
        """

        pA = headA
        pB = headB

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA
