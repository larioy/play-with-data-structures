# -*- encoding: utf-8 -*-


class Solution(object):
    def addSum(self, num1, num2):
        while num2 != 0:
            temp = num1 ^ num2
            num2 = (num1 & num2) << 1   # 注意点: 使用临时变量， 不能在与和或的过程中修改num1和num2
            num1 = temp & 0xFFFFFFFF
        return num1


if __name__ == "__main__":
    s = Solution()
    num1, num2 = 1, 4
    print("{}与{}的和为: {}".format(num1, num2, s.addSum(num1, num2)))
