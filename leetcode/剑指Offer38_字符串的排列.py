"""
@author: Jim
@project: crazy_arithmetic
@file: 剑指Offer38_字符串的排列.py
@time: 2021/5/29 15:58
@desc:

    https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/

   输入一个字符串，打印出该字符串中字符的所有排列。
   你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
"""

from typing import List

class Solution:
    def permutation(self, s: str) -> List[str]:

        s = list(s)
        s_len = len(s)
        result = []

        def dfs(x):
            """ 固定第x位的值

            """

            if x == s_len - 1:
                result.append("".join(s))
                return

            repeat_set = set()
            for i in range(x, s_len):

                if s[i] in repeat_set: continue

                repeat_set.add(s[i])

                s[i], s[x] = s[x], s[i]

                dfs(x + 1)

                s[i], s[x] = s[x], s[i]

        dfs(0)
        return result



if __name__ == '__main__':

    s = Solution()
    ret = s.permutation("bbc")
    print(ret)
