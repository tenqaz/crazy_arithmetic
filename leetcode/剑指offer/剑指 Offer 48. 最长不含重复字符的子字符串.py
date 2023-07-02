"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/7/1 22:38
@desc:
    https://leetcode.cn/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        cache = set()

        q = 0
        res = 0
        s_len = len(s)
        for i in range(s_len):
            if i != 0:
                cache.remove(s[i - 1])

            while q < s_len and s[q] not in cache:
                cache.add(s[q])
                q += 1

            res = max(res, q - i)

        return res


if __name__ == '__main__':
    # 3
    # print(Solution().lengthOfLongestSubstring("abcabcbb"))

    # 1
    # print(Solution().lengthOfLongestSubstring("bbbbb"))

    # 3
    print(Solution().lengthOfLongestSubstring("pwwkew"))
