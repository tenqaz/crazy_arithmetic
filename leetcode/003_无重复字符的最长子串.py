"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2022/12/18 16:25
@desc:
    https://leetcode.cn/problems/longest-substring-without-repeating-characters/

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            滑动窗口+双指针
            使用滑动窗口记录当前最长字串，p_right往后移动，如果后面的字符包含在最长字串中，左边的
        """

        slide_windows = set()
        s_len = len(s)
        ret_max = 0
        p_right = 0
        for i in range(s_len):
            if i > 0:
                slide_windows.remove(s[i - 1])

            while p_right < s_len and s[p_right] not in slide_windows:
                slide_windows.add(s[p_right])
                p_right += 1

            ret_max = max(ret_max, p_right - i)

        return ret_max


if __name__ == '__main__':
    # 3
    # s = "abcabcbb"

    # 1
    s = "bbbbb"
    ret = Solution().lengthOfLongestSubstring(s)
    print(ret)
