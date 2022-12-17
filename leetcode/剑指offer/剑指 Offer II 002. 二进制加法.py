#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File: 剑指 Offer II 002. 二进制加法.py
@Time: 2022/12/17 12:02:54
@Author: Jim
@Contact: zhengwenfeng37@gmail.com
@Desc: 
    https://leetcode.cn/problems/JFETK5/


    通过循环，从两个数的后面开始相加
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len, b_len = len(a), len(b)
        max_len = max(a_len, b_len)

        ret = ""
        jinwei = 0
        for i in range(max_len):

            a_tmp, b_tmp = 0, 0
            if i < a_len:
                a_tmp = int(a[a_len - i - 1])
            if i < b_len:
                b_tmp = int(b[b_len - i - 1])

            binary_sum = a_tmp + b_tmp + jinwei
            jinwei = binary_sum // 2
            ret = str(binary_sum % 2) + ret

        if jinwei:
            ret = "1" + ret

        return ret


if __name__ == '__main__':

    # result: 101
    # a = "11"
    # b = "10"

    # result: 10101
    a = "1010"
    b = "1011"

    ret = Solution().addBinary(a, b)
    print(ret)