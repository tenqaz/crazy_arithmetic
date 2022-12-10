"""
@author: Jim
@project: crazy_arithmetic
@file: 22_括号生成.py
@time: 2020/1/31 12:05
@desc:

    https://leetcode-cn.com/problems/generate-parentheses/
    
"""

from typing import List


class Solution:

    def _gen(self, left: int, right: int, pattern_str: str):
        """

        Args:
            left:
            right:
            pattern_str:

        Returns:

        """

        if left == 0 and right == 0:
            self.results.append(pattern_str)
            return

        if left > 0:
            self._gen(left - 1, right, pattern_str + "(")

        if right > left and right > 0:
            self._gen(left, right - 1, pattern_str + ")")

    def generateParenthesis(self, n: int) -> List[str]:
        """
            DFS 递归
        Args:
            n:

        Returns:

        """

        self.results = []

        self._gen(n, n, "")

        return self.results

if __name__ == '__main__':
    solution = Solution()
    result = solution.generateParenthesis(3)
    print(result)
