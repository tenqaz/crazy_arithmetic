"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/24 17:29
@desc:
    https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/?envType=study-plan-v2&envId=coding-interviews

    1. 使用有序的字典计数
    2. 不需要有序的字典，字典的value记录索引，去最小索引即为第一次出现
    3. 使用字典+队列
"""

from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> str:
        """
          使用字典记录次数，也可以直接使用内置库Counter，这里没用
        """

        cache_dict = OrderedDict()

        for i in s:
            if i in cache_dict:
                cache_dict[i] += 1
            else:
                cache_dict[i] = 1

        if cache_dict:
            for key, value in cache_dict.items():
                if value == 1:
                    return key

        return " "

if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar(""))
