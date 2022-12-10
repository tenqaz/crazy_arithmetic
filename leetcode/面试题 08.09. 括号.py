"""
@author: Jim
@project: crazy_arithmetic
@file: 面试题 08.09. 括号.py
@time: 2021/5/29 17:41
@desc:

https://leetcode-cn.com/problems/bracket-lcci/
    括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。

说明：解集不能包含重复的子集。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def dfs(tmp, left, right):

            if right > left or left > n:
                return

            if left + right == 2 * n:
                result.append(tmp)

            dfs(tmp + "(", left + 1, right)
            dfs(tmp + ")", left, right + 1)

        dfs("", 0, 0)

        return result


if __name__ == '__main__':
    s = Solution()
    ret = s.generateParenthesis(3)
    print(ret)
