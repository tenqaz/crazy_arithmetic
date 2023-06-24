"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/24 17:59
@desc:
    
"""
from typing import List

from tools.tree_node_tools import make_Treelist


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:

        ret = []
        queue = []
        queue.append(root)

        while queue:
            item = queue.pop(0)

            ret.append(item.val)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)

        return ret


if __name__ == '__main__':
    head = make_Treelist([3, 9, 20, None, None, 15, 7])
    s = Solution()
    ret = s.levelOrder(head)
    print(ret)
