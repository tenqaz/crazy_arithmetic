"""
@author: Jim
@project: crazy_arithmetic
@time: 2019/12/1 17:09
@desc: 用队列实现栈

使用两个队列A,B，将A队列的中的数据移动到b队列中，A队列保存最后一个数据，并弹出，再将两个队列数据交换。

两边倒

"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        ret = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1

        return ret

    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        ret = self.queue1.pop()

        self.queue2.append(ret)
        self.queue1, self.queue2 = self.queue2, self.queue1

        return ret

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if not self.queue1:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)
