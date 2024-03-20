"""
@author: Jim
@project: crazy_arithmetic
@file: 111_二叉树的最小深度.py
@time: 2020/1/30 0:09
@desc:  
   给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

"""
from tools.tree_node_tools import make_Treelist


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def minDepth(self, root: TreeNode) -> int:
        """
            DFS 递归解法
        Args:
            root:

        Returns:

        """

        if not root: return 0

        if not root.left: return self.minDepth(root.right) + 1
        if not root.right: return self.minDepth(root.left) + 1

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        return min(left, right) + 1

    def minDepth(self, root: TreeNode) -> int:
        """
            BFS 解法
        Args:
            root:

        Returns:

        """

        if not root: return 0

        queue = [root]
        min_result = 0

        while queue:

            queue_len = len(queue)
            min_result += 1

            for index in range(queue_len):

                node = queue.pop(0)

                if not node.left and not node.right: return min_result

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)


if __name__ == '__main__':
    # result: 3
    data = [3, 9, 20, None, None, 15, 7]
    head = make_Treelist(data)

    s = Solution()
    ret = s.minDepth(head)
    print(ret)