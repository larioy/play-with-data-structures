# -*- encoding: utf-8 -*-


class MyStack(object):
    def __init__(self):
        self.queue = []

    def push(self, data):
        self.queue.append(data)
        for _ in range(len(self.queue) -1):
            oldest = self.queue.pop(0)
            self.queue.append(oldest)

    def pop(self):
        self._shift()
        return self.queue.pop(0)

    def _shift(self):
        if len(self.queue2) == 0:
            if len(self.queue1) > 0:
                self.queue2.insert(0, self.queue1.pop())

    def size(self):
        return len(self.queue2) + len(self.queue1)


if __name__ == "__main__":
    mystack = MyStack()
    for i in range(3):
        mystack.push(i)
        print(mystack.queue)
