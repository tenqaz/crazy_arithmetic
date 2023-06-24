"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/23 16:04
@desc:
    https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof/?envType=study-plan-v2&envId=coding-interviews
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """ 利用了语言特性 """
        s_list = s.split()
        s_list.reverse()
        return " ".join(s_list)


if __name__ == '__main__':
    s = Solution()
    # ret = s.reverseWords("the sky is blue")
    ret = s.reverseWords("  hello world!  ")
    print(ret)
