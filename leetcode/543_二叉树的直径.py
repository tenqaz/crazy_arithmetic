#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File: 543_二叉树的直径.py
@Time: 2022/12/12 19:21:14
@Author: Jim
@Contact: zhengwenfeng37@gmail.com
@Desc: 

https://leetcode.cn/problems/diameter-of-binary-tree/
'''

import sys
sys.path.append("../")

from tools.tree_node_tools import *
from typing import Optional



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        self.max_len = 1
        
        def gen(root: Optional[TreeNode]):
            if not root:
                return 0

            left_len = gen(root.left)
            right_len = gen(root.right)

            self.max_len = max(self.max_len, left_len+right_len+1)
            
            return max(left_len, right_len) + 1

        gen(root)
        return self.max_len - 1
        


if __name__ == '__main__':
    root = [1, 2, 3, 4, 5]
    head = make_Treelist(root)

    s = Solution()
    ret = s.diameterOfBinaryTree(head)

    print(ret)