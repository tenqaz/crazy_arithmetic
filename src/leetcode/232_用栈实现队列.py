# -*- coding: utf-8 -*-

"""
@author: Jim
@project: crazy_arithmetic
@time: 2019/12/5 10:25
@desc:

    使用堆栈实现队列

    用两个栈去实现。分为输入栈和输出栈，将输入栈push到输出栈，输出栈的栈顶就是队列的输出.

    两个栈两边倒
"""

from __future__ import annotations


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input_stack = []
        self.output_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.input_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

        return self.output_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

        return self.output_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.input_stack and not self.output_stack:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

print(param_2)
print(param_3)
print(param_4)
