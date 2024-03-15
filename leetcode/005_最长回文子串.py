"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2022/12/18 16:49
@desc:
    https://leetcode.cn/problems/longest-palindromic-substring/

    
思路：
    1. 遍历字符串每一个元素作为回文的中心。
    2. 如果回文是奇数，则中心有一个元素，如果为偶数，则中心有两个元素。然后分别获得回文的字符串。
    3. 遍历完成后，获取最大长度的回文字符串。
"""


class Solution:
    def func2(self, s, left, right):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1

    def longestPalindrome2(self, s: str) -> str:
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
    

    def func(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1: right]

    def longestPalindrome(self, s: str) -> str:
        rst = ""

        for i in range(len(s)):
            s1 = self.func(s, i, i)
            s2 = self.func(s, i, i + 1)

            rst = max(rst, s1, s2, key=len)

        return rst


if __name__ == '__main__':
    s = "babad"

    ret = Solution().longestPalindrome(s)
    print(ret)
