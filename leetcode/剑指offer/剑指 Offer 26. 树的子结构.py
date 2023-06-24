"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/24 19:21
@desc:
    https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/?envType=study-plan-v2&envId=coding-interviews
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        queue = [A]

        while queue:
            item = queue.pop(0)

            if item.val == B.val:

