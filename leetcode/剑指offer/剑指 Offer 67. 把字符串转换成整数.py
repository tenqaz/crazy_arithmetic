"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/7/15 20:07
@desc:
    https://leetcode.cn/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/?envType=study-plan-v2&envId=coding-interviews
"""

INT_MAX = 2 ** 31 - 1

class Solution:
    def strToInt(self, str: str) -> int:

        str_len = len(str)
        for i in range(str_len):
            if str[i] == "-" or "9" >= str[i] >= "0":
                break
            elif str[i] == " ":
                continue
            else:
                return 0

        sign = 1
        if str[i] == "-":
            i += 1
            sign = -1

        res = 0
        for i in range(i, str_len):
            if not str[i].isdigit():
                break
            res = res * 10 + int(str[i])



        if sign == 1:
            res = min(res, INT_MAX)
        else:
            res = min(res, -INT_MAX)

        res *= sign

        return res


if __name__ == '__main__':
    print(Solution().strToInt("42"))
    print(Solution().strToInt("        -42"))
    print(Solution().strToInt("4193 with words"))
    print(Solution().strToInt("words and 987"))
    print(Solution().strToInt("-91283472332"))


