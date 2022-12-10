"""
@author: Jim
@project: crazy_arithmetic
@file: 139_单词拆分.py
@time: 2021/9/20 18:37
@desc:  
    https://leetcode-cn.com/problems/word-break/
"""

from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """ 动态规划

        """

        s_bool = [False for i in range(len(s))]
        s_len = len(s)
        for i in range(s_len):
            for j in range(i, s_len):
                if s_bool[i] and s[i: j] in wordDict:
                    s_bool[i] = True

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        """ 贪心，只要符合，就取单词，这样不行。

        错误写法

        """

        cur_word = ""
        for i in s:
            cur_word += i

            if cur_word in wordDict:
                cur_word = ""

        if cur_word:
            return False

        return True


s = "aaaaaaa"
word_Dict = ["aaaa", "aaa"]
solaution = Solution()
ret = solaution.wordBreak(s, word_Dict)
print(ret)
