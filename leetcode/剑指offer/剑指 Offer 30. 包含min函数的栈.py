"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/23 16:30
@desc:
    https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof/

    使用辅助栈，每次push值时，保存当前时刻，最小值。
"""

import math


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
