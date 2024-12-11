#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File: 151_反转字符串中的单词.py
@Time: 2024/04/22 16:42:11
@Author: Jim
@Contact: zhengwenfeng37@gmail.com
@Desc: 

    目前的解法时间复杂度是O(N),如果想要将时间复杂度改成O(1)，解法如下：
    1. 先将整个字符串给翻转过来
    2. 然后再遍历逐个将单词翻转过来

    因为python的字符串特性是不可修改的,所以无法做到,需要将字符串打散到一个字符串列表才行。
    只有C或C++的字符串是数组可以实现。

'''




class Solution:

    def reverseWords(self, s: str) -> str:
        """
            空间复杂度：O(n)
            时间复杂度：O(n)
        """
        s_split = s.split()
        s_split.reverse()
        return ' '.join(s_split)


if __name__ == '__main__':
    # "blue is sky the"
    s = "the sky is blue"

    print(Solution().reverseWords(s))
