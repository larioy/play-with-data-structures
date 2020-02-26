# -*- encoding: utf-8 -*-

"""
给定两个序列， 判断其中的一个是另外一个的栈的出栈序列
"""


class Solution(object):
    def StackConfirm(self, pushStack, popStack):
        pushLen = len(pushStack)
        popLen = len(popStack)

        if pushLen != popLen:
            return False

        stack = []
        for ele in pushStack:
            stack.append(ele)
            while stack and stack[-1] == popStack[0]:
                stack.pop()
                popStack.pop(0)    # 这种方式会改变输入的原数组， 可以使用下标的方式进行
        if len(stack) == 0:
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    pushStack = [1, 2, 3, 4, 5]
    popStack = [4, 5, 3, 2, 1]
    print(s.StackConfirm(pushStack, popStack))
