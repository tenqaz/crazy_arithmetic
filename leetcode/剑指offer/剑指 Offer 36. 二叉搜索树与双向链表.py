"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/24 22:44
@desc:
    
"""
from tools.tree_node_tools import make_Treelist, print_Treelist


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def in_order(root):
            if root is None:
                return

            if root.left:
                in_order(root.left)

            order_list.append(root)

            if root.right:
                in_order(root.right)

        order_list = []
        in_order(root)



if __name__ == '__main__':
    root = [4, 2, 5, 1, 3]
    head = make_Treelist(root)

    s = Solution()
    ret = s.treeToDoublyList(head)
