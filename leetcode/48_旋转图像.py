#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File: 48_旋转图像.py
@Time: 2024/04/22 18:49:03
@Author: Jim
@Contact: zhengwenfeng37@gmail.com
@Desc: 
'''



from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        解决思路：先将矩阵从斜对角进行翻转，然后再逐行进行翻转。
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i] = list(reversed(matrix[i]))


if __name__ == '__main__':
    # [[7,4,1],[8,5,2],[9,6,3]]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    Solution().rotate(matrix)
    print(matrix)
