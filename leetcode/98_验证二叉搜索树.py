"""
@author: Jim
@project: crazy_arithmetic
@file: 98_验证二叉搜索树.py
@time: 2019/12/10 14:28
@desc:

    验证二叉搜索树

    判断一个二叉树是否是二叉搜索树

    1. 中序遍历等于排序
    2. 递归，左节点小于父节点，右节点大于父节点。
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def gen(self, root: TreeNode) -> List:
        """  中旬遍历递归获取列表

        Args:
            root:

        Returns:

        """

        if root is None:
            return []

        return self.gen(root.left) + [root.val] + self.gen(root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        """
            使用中序遍历打成一个数组，然后判断该数组是否有序即可. O(n)

        Args:
            root:

        Returns:

        """

        in_order_list = self.gen(root)

        return in_order_list == list(sorted(set(in_order_list)))  # 这里的内部操作比较多

    def helper(self, root: TreeNode):
        """
            递归中序遍历
        Args:
            root:

        Returns:

        """
        if root is None:
            return True

        if not self.helper(root.left):
            return False

        if self.prev and self.prev.val >= root.val:
            return False

        self.prev = root

        return self.helper(root.right)

    def isValidBST2(self, root: TreeNode):
        """
            使用中序遍历

        Args:
            root:

        Returns:

        """

        self.prev = None
        return self.helper(root)

    def gen3(self, root: TreeNode, min: int, max: int):
        """

            递归遍历，左节点会小于父节点，右节点大于父节点

        Args:
            root:
            min:
            max:

        Returns:

        """

        if root is None:
            return True

        val = root.val
        if min is not None and val <= min: return False
        if max is not None and val >= max: return False

        return self.gen3(root.left, min, val) and self.gen3(root.right, val, max)

    def isValidBST3(self, root: TreeNode) -> bool:
        """
            使用递归判断左边的最大值小于根结点，右边的最小值大于根结点

        Args:
            root:

        Returns:

        """

        return self.gen3(root, None, None)


def init1():
    # data = [2, 1, 3]
    data2 = TreeNode(2)
    data1 = TreeNode(1)
    data3 = TreeNode(3)

    data2.left = data1
    data2.right = data3

    return data2


def init2():
    data = [1, 1]
    data0 = TreeNode(1)
    data1 = TreeNode(1)

    data0.left = data1

    return data0


def init3():
    data = [0, None, -1]
    data0 = TreeNode(0)
    data1 = TreeNode(-1)

    data0.left = None
    data0.right = data1

    return data0


if __name__ == '__main__':

    # root = init1()
    # root = init2()  # false
    root = init3()  # true

    solution = Solution()
    # rst = solution.isValidBST(root)
    rst = solution.isValidBST3(root)
    print(rst)
