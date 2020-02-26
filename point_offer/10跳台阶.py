# -*- encoding: utf-8 -*-


"""
跳台阶解法： 因为是只可以跳1或2步， 所以第i个台阶有第i-1和i-2的台阶的跳法的相加
所以可以从尾到前进行推理， 然后得到初始的条件，

"""


class Solution(object):
    def __init__(self):
        pass

    def JumpStep(self, n):
        a = 0
        b = 1
        while n:
            c = a + b
            a = b
            b = c
            n = n - 1
        return a


if __name__ == "__main__":
    s = Solution()
    print(s.JumpStep(5))
