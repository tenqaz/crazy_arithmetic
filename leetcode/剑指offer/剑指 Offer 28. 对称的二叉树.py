"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/24 19:40
@desc:
    
"""
from tools.tree_node_tools import make_Treelist


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric3(self, root: TreeNode) -> bool:
        """
            BFS，获取每一行的数组，再判断该数组是不是对称的。

            时间复杂度：O(n)
            空间复杂度：O(n)
        """

        queue = [root]

        while queue:

            line = []
            for i in range(len(queue)):
                item = queue.pop(0)

                if item is None:
                    line.append(item)
                    continue

                line.append(item.val)

                if item is not None:
                    queue.append(item.left)
                    queue.append(item.right)

            p, q = 0, len(line) - 1
            while p < q:
                if line[p] != line[q]:
                    return False

                p += 1
                q -= 1

        return True

    def isSymmetric2(self, root: TreeNode) -> bool:
        """ 递归 """
        pass

    def isSymmetric(self, root: TreeNode) -> bool:
        """ 迭代 """
        pass


if __name__ == '__main__':
    # True
    # root = [1, 2, 2, 3, 4, 4, 3]

    # False
    root = [1, 2, 2, None, 3, None, 3]
    head = make_Treelist(root)

    s = Solution()
    ret = s.isSymmetric(head)
    print(ret)
