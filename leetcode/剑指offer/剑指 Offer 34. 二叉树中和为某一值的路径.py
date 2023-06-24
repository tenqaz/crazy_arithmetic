"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/24 22:14
@desc:
    https://leetcode.cn/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        def _dfs(root: TreeNode, level_sum: 0):
            if root is None:
                return




