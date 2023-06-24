"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/24 23:18
@desc:
    
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """ 先中序遍历获取到一个排序数组，再取第k大的数"""


        def in_order(root):
            pass
