"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/24 18:26
@desc:
    https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/?envType=study-plan-v2&envId=coding-interviews
"""
from typing import List

from tools.tree_node_tools import make_Treelist


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
            BFS解法
        """
        if not root:
            return []

        ret = []
        queue = [root]

        direct = False

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

            if direct:
                line_list.reverse()

            direct = not direct

            ret.append(line_list)

        return ret


if __name__ == '__main__':
    head = make_Treelist([3, 9, 20, None, None, 15, 7])
    # head = make_Treelist([1, 2, 3, 4, None, None, 5])
    s = Solution()
    ret = s.levelOrder(head)
    print(ret)
