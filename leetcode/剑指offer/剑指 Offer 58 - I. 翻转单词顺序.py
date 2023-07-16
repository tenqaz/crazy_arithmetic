"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/23 16:04
@desc:
    https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof/?envType=study-plan-v2&envId=coding-interviews
"""

import collections


class Solution:
    def reverseWords2(self, s: str) -> str:
        """ 利用了语言特性 """
        s_list = s.split()
        s_list.reverse()
        return " ".join(s_list)

    def reverseWords(self, s: str):
        left, right = 0, len(s) - 1

        while left <= right and s[left] == ' ':
            left += 1

        while left <= right and s[right] == ' ':
            right -= 1

        word = []
        deque = collections.deque()
        while left <= right:
            if s[left] == ' ' and word:
                deque.appendleft("".join(word))
                word.clear()
            elif s[left] != ' ':
                word.append(s[left])

            left += 1

        deque.appendleft("".join(word))

        return " ".join(deque)


if __name__ == '__main__':
    s = Solution()
    # ret = s.reverseWords("the sky is blue")
    ret = s.reverseWords("example   good a")
    print(ret)


