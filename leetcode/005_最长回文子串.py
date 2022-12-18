"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2022/12/18 16:49
@desc:
    https://leetcode.cn/problems/longest-palindromic-substring/
"""


class Solution:
    def func(self, s, left, right):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        start = end = 0
        for i in range(s_len):
            left1, right1 = self.func(s, i, i)
            left2, right2 = self.func(s, i, i + 1)

            if right1 - left1 > end - start:
                start, end = left1, right1

            if right2 - left2 > end - start:
                start, end = left2, right2

        return s[start: end + 1]


if __name__ == '__main__':
    s = "babad"

    ret = Solution().longestPalindrome(s)
    print(ret)
