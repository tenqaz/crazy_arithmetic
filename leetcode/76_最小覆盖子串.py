#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File: 76_最小覆盖子串.py
@Time: 2024/04/23 11:14:46
@Author: Jim
@Contact: zhengwenfeng37@gmail.com
@Desc: 
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # 将目前字符串打散在字典中。
        need = Counter(t)
        # 当前窗口字符串计数
        windows = Counter()
        
        # 使用left和right来控制窗口的左右边界
        left = right = 0
        # 有效字符数
        valid = 0
        # 最小长度的起始位置和长度
        start, length = 0, float('inf')

        while right < len(s):

            # 扩容
            item = s[right]
            right += 1

            if item in need:
                windows[item] += 1
                if windows[item] == need[item]:
                    valid += 1

            # 缩容
            while valid == len(need):
                # 获取最小长度
                if right - left < length:
                    start, length = left, right - left

                # 移除窗口项
                item = s[left]
                left += 1
                if item in need:
                    windows[item] -= 1
                    if windows[item] < need[item]:
                        valid -= 1

        return "" if length == float('inf') else s[start:start + length]


if __name__ == '__main__':
    # BANC
    s = "ADOBECODEBANC"
    t = "ABC"

    print(Solution().minWindow(s, t))
