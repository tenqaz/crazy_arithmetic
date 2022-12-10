"""
@author: Jim
@project: crazy_arithmetic
@file: 52_N皇后二.py
@time: 2020/1/31 13:39
@desc:  
    
"""

from typing import List


class Solution:

    def _gen(self, row: int, cur_status: List[int]):

        if row == self.n:
            self.result.append(cur_status)
            return

        for col in range(self.n):

            # 剪枝
            if col in self.col or col + row in self.pie or row - col in self.na:
                continue

            # 符合条件
            self.col.add(col)
            self.pie.add(col + row)
            self.na.add(row - col)

            # 递归每一种情况
            self._gen(row + 1, cur_status + [col])

            # 回溯
            self.col.remove(col)
            self.pie.remove(col + row)
            self.na.remove(row - col)

    def totalNQueens(self, n: int) -> List[List[str]]:
        self.col = set()
        self.pie = set()
        self.na = set()
        self.n = n
        self.result = []

        self._gen(0, [])

        return len(self.result)

if __name__ == '__main__':
    solution = Solution()
    print(solution.totalNQueens(4))