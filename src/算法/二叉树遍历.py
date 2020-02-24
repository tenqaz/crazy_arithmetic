"""
@author: Jim
@project: crazy_arithmetic
@file: 二叉树遍历.py
@time: 2020/2/23 21:02
@desc:  
    
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Traverse:

    def front(self, root: TreeNode):
        """
            前序遍历
        Args:
            root:

        Returns:

        """

        if not root:
            return None

        print(root.val)
        self.front(root.left)
        self.front(root.right)

    def mid(self, root: TreeNode):
        """
            中序遍历
        Args:
            root:

        Returns:

        """

        if not root:
            return None

        self.mid(root.left)
        print(root.val)
        self.mid(root.right)

    def back(self, root: TreeNode):
        """
            后续遍历
        Args:
            root:

        Returns:

        """
        if not root:
            return None
        
        self.back(root.left)
        self.back(root.right)
        print(root.val)

    def dfs(self, root: TreeNode):
        """
            深度优先遍历
        Args:
            root:

        Returns:

        """

if __name__ == '__main__':
    traverse = Traverse()
    traverse.front()
