"""
@author: Jim
@project: crazy_arithmetic
@file: 258_各位相加.py
@time: 2020/2/22 15:27
@desc:  
    https://leetcode-cn.com/problems/add-digits/
"""


class Solution:
    def addDigits(self, num: int) -> int:

        while num > 9:

            res = 0
            while num > 9:
                res += num % 10
                num = num // 10

            res += num
            num = res

        return num


if __name__ == '__main__':
    solution = Solution()
    res = solution.addDigits(38)
    print(res)
