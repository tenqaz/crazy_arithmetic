"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/23 16:12
@desc:
    https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
"""


class CQueue:

    def __init__(self):
        self.input_stack = []
        self.outpu_stack = []

    def appendTail(self, value: int) -> None:
        self.input_stack.append(value)

    def deleteHead(self) -> int:
        if not self.outpu_stack:
            while self.input_stack:
                self.outpu_stack.append(self.input_stack.pop())

        if self.outpu_stack:
            return self.outpu_stack.pop()
        else:
            return -1


# Your CQueue object will be instantiated and called as such:
obj = CQueue()
obj.appendTail(1)
obj.appendTail(2)
obj.appendTail(3)
obj.appendTail(4)
param_2 = obj.deleteHead()
print(param_2)