"""
@author: Jim
@project: crazy_arithmetic
@file: 104_二叉树的最大深度.py
@time: 2020/1/29 18:03
@desc:  

    给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        """
            DFS 解法
        Args:
            root:

        Returns:

        """

        if not root: return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth(self, root: TreeNode) -> int:
        """
            BFS 解法
        Args:
            root:

        Returns:

        """

        if not root: return 0

        queue = [root]
        max = 0

        while queue:

            max += 1
            que_len = len(queue)

            for index in range(que_len):

                node = queue.pop(0)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return max
