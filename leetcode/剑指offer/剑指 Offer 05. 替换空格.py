"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/22 15:19
@desc:
    https://leetcode.cn/problems/ti-huan-kong-ge-lcof/
"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        ret_list = []
        for i in s:
            if i == " ":
                ret_list.append("%20")
            else:
                ret_list.append(i)

        return "".join(ret_list)


if __name__ == '__main__':
    s = "We are happy."
    solution = Solution()
    ret = solution.replaceSpace(s)
    print(ret)
