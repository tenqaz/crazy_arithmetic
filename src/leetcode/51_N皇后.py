"""
@author: Jim
@project: crazy_arithmetic
@file: 51_N皇后.py
@time: 2020/1/31 12:20
@desc:  
    https://leetcode-cn.com/problems/n-queens/

    规律. pie = row + col = n
          na = row - col = n

"""

from typing import List
from pprint import pprint


class Solution:

    def _print_result(self):
        result = []

        for solution in self.result:
            solution_list = []
            for index in solution:
                result_str = "." * (index)
                result_str += "Q"
                result_str += "." * (self.n - index - 1)

                solution_list.append(result_str)

            result.append(solution_list)

        return result

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

            # 继续递归
            self._gen(row + 1, cur_status + [col])

            # 复位
            self.col.remove(col)
            self.pie.remove(col + row)
            self.na.remove(row - col)

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.col = set()
        self.pie = set()
        self.na = set()
        self.n = n
        self.result = []

        self._gen(0, [])

        return self._print_result()


if __name__ == '__main__':
    solution = Solution()
    result = solution.solveNQueens(4)
    pprint(result)
