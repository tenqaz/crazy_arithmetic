"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/25 20:43
@desc:
    
"""

MOD = 10 ** 9 + 7


class Solution:

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        pre1, pre2 = 1, 1

        for i in range(2, n):
            pre1, pre2 = pre2, pre1 + pre2

        return pre2 % MOD


if __name__ == '__main__':
    print(Solution().fib(45))
