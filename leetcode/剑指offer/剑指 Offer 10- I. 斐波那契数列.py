"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/25 20:43
@desc:
    
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)
