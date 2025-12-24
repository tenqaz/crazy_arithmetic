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

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            自己想的实现方式
            1. 使用cache验证是否包含重复字符
            2. 使用p、q 来表示双指针
            3. 如果不存在重复字符，则q+1，并且记录该字符
            4. 如果存在，则p+1，并且删除该字符    
        """
        s_len = len(s)
        if s_len == 0:
            return 0

        cache = set()
        p = 0
        q = 0
        max_len = 0
        while q < s_len:
            if s[q] not in cache:
                max_len = max(max_len, q - p + 1)
                cache.add(s[q])
                q += 1
            else:
                cache.remove(s[p])
                p += 1

        return max_len
    
    def lengthOfLongestSubstring3(self, s: str) -> int:
        """ 滑动窗口实现

        1. 一直遍历到有缓存为止
        2. left 一直向左滑动到缓存不存在为止。
        3. 记录每一次的最大值

        Args:
            s (str): _description_

        Returns:
            int: _description_
        """
        
        left = 0
        max_len = 0
        s_len = len(s)
        cache = set()

        for i in range(s_len):
            
            while s[i] in cache:
                cache.remove(s[left])
                left += 1
            
            max_len = max(max_len, i - left + 1)
            cache.add(s[i])

        return max_len


if __name__ == "__main__":
    # 3
    # s = "abcabcbb"

    # 1
    s = "bbbbb"
    ret = Solution().lengthOfLongestSubstring(s)
    print(ret)
