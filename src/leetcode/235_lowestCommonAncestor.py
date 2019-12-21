"""
@author: Jim
@project: crazy_arithmetic
@file: 235_lowestCommonAncestor.py
@time: 2019/12/16 16:24
@desc:
    二叉搜索树最近公共祖先
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """

            根据 搜索树的规则 左子树所有节点的值都小于根结点，右子树所有节点的值都大于根结点.

            1. 如果两个节点都小于根结点，说明在左子树.
            2. 如果两个节点都大于根结点，说明在右子树.

        Args:
            root:
            p:
            q:

        Returns:

        """
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root
