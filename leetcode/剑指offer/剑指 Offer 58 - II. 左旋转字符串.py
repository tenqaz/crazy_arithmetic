"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/22 15:22
@desc:
    https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


if __name__ == '__main__':
    s = "lrloseumgh"
    k = 6
    solution = Solution()
    ret = solution.reverseLeftWords(s, k)
    print(ret)
