"""
@author: Jim
@project: crazy_arithmetic
@file: 二叉查找树.py
@time: 2020/2/24 12:25
@desc:

    二叉查找树

    该代码没有测试过

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinarySearchTree:

    def find(self, root: TreeNode, target: int) -> TreeNode:
        """

            时间复杂度: O(logn)

        Args:
            root:
            target:

        Returns:

        """

        while root:

            if target < root.val:
                root = root.left
            elif target > root.val:
                root = root.right
            else:
                return root

        return None

    def insert(self, root: TreeNode, target: int):
        """
            插入
        Args:
            root:
            target:

        Returns:

        """

        while root:

            if target < root.val:
                if not root.left:
                    root.left = TreeNode(target)
                    return
                root = root.left
            else:
                if not root.right:
                    root.right = TreeNode(target)
                    return
                root = root.right

    def delete(self, root: TreeNode, target: int):
        """
            删除.  写的不好，以后要修改.绝对有错误

            1. 删除的节点没有子节点，直接删除
            2. 删除的节点只有一个子节点，则直接将该子节点替换删除的节点
            3. 删除的节点有两个以上的子节点，则需要从右子树中查找最小的数替换到删除的节点中。

        Args:
            root:
            target:

        Returns:

        """

        pp = None  # 父节点

        while root and root.val != target:
            pp = root
            if target < root.val:
                root = root.left
            else:
                root = root.right

        if not root: return

        # 要删除的有两个以上的子节点
        if root.left and root.right:
            minp = root.right
            minpp = root

            while minp.left:
                minpp = minp
                minp = minp.left

            root.val = minp.val
            minpp.left = None
            return

        if root.left:  # 如果要删除的有一个节点
            root = root.left
            return
        elif root.right:
            root = root.right
            return

        # 删除的是根结点
        if pp.left:
            pp.left = None
        else:
            pp.right = None
