# -*- coding: utf-8 -*-

"""
@author: Jim
@project: crazy_arithmetic
@time: 2019/12/9 16:56
@desc:
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

    示例 1:

    输入: s = "anagram", t = "nagaram"
    输出: true

    示例 2:

    输入: s = "rat", t = "car"
    输出: false

"""

from __future__ import annotations


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """

            使用sorted对字符串的ascii进行排序，然后再比较.

            快排 O(nlogn)

        Args:
            s(str):
            t(str):

        Returns(bool):

        """

        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        """
            使用字典计数。 O(n)

        Args:
            s(str):
            t(str):

        Returns(bool):

        """

        dict1 = {}
        dict2 = {}

        for i in s:
            dict1[i] = dict1.get(i, 0) + 1

        for i in t:
            dict2[i] = dict2.get(i, 0) + 1

        return dict1 == dict2


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"

    solution = Solution()
    # res = solution.isAnagram(s, t)
    res = solution.isAnagram2(s, t)
    print(res)
