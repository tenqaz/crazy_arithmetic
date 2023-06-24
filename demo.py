"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2022/12/28 17:42
@desc:
    剑指 Offer 05. 替换空格
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
