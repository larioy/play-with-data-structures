# -*- encoding: utf-8 -*-


class Solution(object):
    def __init__(self):
        self.queue = []

    def push(self, val):
        self.queue.append(val)
        for i in range(len(self.queue)):   # 注意python的range达到的是len-1
            self.queue.append(self.queue.pop(0))

    def pop(self):
        if len(self.queue) == 0:
            return None
        self.queue.pop(0)

    def top(self):
        if len(self.queue):
            return self.queue[0]