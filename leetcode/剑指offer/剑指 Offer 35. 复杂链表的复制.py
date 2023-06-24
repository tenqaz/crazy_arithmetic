"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/23 11:56
@desc:
    https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.cache_node = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        """ 哈希表+回溯 """

        if not head:
            return

        if head in self.cache_node:
            return self.cache_node[head]

        new_node = Node(x=head.val)
        self.cache_node[head] = new_node
        new_node.next = self.copyRandomList(head.next)
        new_node.random = self.copyRandomList(head.random)

        return new_node

