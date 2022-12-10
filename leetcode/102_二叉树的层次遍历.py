"""
@author: Jim
@project: crazy_arithmetic
@file: 102_二叉树的层次遍历.py
@time: 2020/1/18 15:13
@desc:
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
            BFS解法

        Args:
            root:

        Returns:
        """

        if not root: return []

        queue = [root]
        results = []

        while queue:

            level_list = []
            queue_len = len(queue)

            for index in range(queue_len):

                item = queue.pop(0)

                level_list.append(item.val)
                if item.left: queue.append(item.left)
                if item.right: queue.append(item.right)

            results.append(level_list)

        return results

    def _dfs(self, node: TreeNode, level: int):

        if len(self.results) < level + 1:
            self.results.append([])

        if node.left: self._dfs(node.left, level + 1)
        if node.right: self._dfs(node.right, level + 1)

        self.results[level].append(node.val)

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        """
            DFS 解法
        Args:
            root:

        Returns:

        """
        if not root: return []

        self.results = []

        self._dfs(root, 0)

        return self.results
