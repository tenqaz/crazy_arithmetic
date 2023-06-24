"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/24 18:11
@desc:
    
"""
from typing import List

from tools.tree_node_tools import make_Treelist


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        """
            BFS解法
        """
        if not root:
            return []

        ret = []
        queue = [root]

        while queue:

            line_list = []
            queue_len = len(queue)
            for _ in range(queue_len):
                item = queue.pop(0)
                line_list.append(item.val)

                if item.left:
                    queue.append(item.left)

                if item.right:
                    queue.append(item.right)

            ret.append(line_list)

        return ret

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """ DFS """

        def _dfs(root: TreeNode, level):
            if root is None:
                return

            if len(self.result) < level + 1:
                self.result.append([])

            self.result[level].append(root.val)

            if root.left:
                _dfs(root.left, level + 1)

            if root.right:
                _dfs(root.right, level + 1)

        self.result = []

        _dfs(root, 0)

        return self.result


if __name__ == '__main__':
    head = make_Treelist([3, 9, 20, None, None, 15, 7])
    s = Solution()
    ret = s.levelOrder(head)
    print(ret)
