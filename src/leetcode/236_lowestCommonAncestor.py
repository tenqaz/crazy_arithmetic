"""
@author: Jim
@project: crazy_arithmetic
@file: 236_lowestCommonAncestor.py
@time: 2019/12/16 11:11
@desc:

    二叉树最近公共祖先
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """

        1. 如果左边没有，则在右边.
        2. 如果右边没有，则在左边
        3. 如果左右两边都有，则是该root节点

        Args:
            root:
            p:
            q:

        Returns:

        """

        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root
