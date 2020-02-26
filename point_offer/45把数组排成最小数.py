# -*- encoding: utf-8 -*-
"""
将数字数组进行排序， 排序得到最小的数字
1、将数字转换为字符串
2、使用冒泡排序， 排序的对象为两个元素的合并字符串
第一次排序得到最大的元素， 放到末尾
第二次得到次大的元素放到第倒数第二
"""


class Solution:
    def theMax(self, str1, str2):
        """
        定义字符串比较函数
        """
        return str1 if str1+str2 > str2+str1 else str2

    def PrintMinNumber(self, numbers):
        """
        使用冒泡进行排序(把最大的放最后)
        """
        string = [str(num) for num in numbers]
        strLen = len(string)
        for i in range(strLen)[::-1]:
            for j in range(i):
                maxStr = self.theMax(string[i], string[j])
                if maxStr == string[j]:
                    string[j], string[i] = string[i], string[j]
        string = ''.join(string)
        return string


if __name__ == "__main__":
    s = Solution()
    arr = [5, 2, 67, 9, 8, 34, 1]
    print(s.PrintMinNumber(arr))

    arr = [3, 32, 321]
    print(s.PrintMinNumber(arr))

