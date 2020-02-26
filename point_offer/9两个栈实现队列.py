# -*- encoding: utf-8 -*-

"""
用栈实现队列
栈： 存最新取最新， append/pop
队列： 存最新取最旧
存: 队列一： append()存最新， 队列里面状态： 最旧----->最新
中间转换： 队列一： pop弹出 弹出顺序：最新---->最旧，  队列二： append存  最新---->最旧
取： 队列二： pop最旧
"""


class Solution(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val):
        self.stack1.append(val)  # 实现最新的放在最后

    def __shift(self):
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())   # 实现将老的放在最后面

    def pop(self):
        return self.stack2.pop()  # 从后面弹出最老的

    def empty(self):
        if len(self.stack1) + len(self.stack2) > 0:
            return True
        else:
            return False

    def peek(self):
        self.__shift()
        return self.queue2[-1]
