"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/25 20:56
@desc:
    https://leetcode.cn/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/?envType=study-plan-v2&envId=coding-interviews
"""

MOD = 10**9 + 7

class Solution:
    def numWays2(self, n: int) -> int:
        """ 超时 """
        if n == 0:
            return 1

        if n == 1 or n == 2:
            return n

        return (self.numWays(n - 1) + self.numWays(n - 2)) % MOD

    def numWays(self, n: int) -> int:
        """ 滚动数组 """

        p, q = 1, 1

        for i in range(1, n):
            p, q = q, p + q

        return q % MOD


if __name__ == '__main__':
    print(Solution().numWays2(7))
    print(Solution().numWays2(0))
