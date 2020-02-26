# -*- encoding: utf-8 -*-

"""
实现方式：
设置一个字典存储， key为字符串的元素， value为该元素在字符串中的元素
一个一维数组， 存储每一个字符串元素以自己结尾的最大不重复子串长度
具体实现见代码
"""


class Solution(object):

    def maxLenNoRepeatSubStr(self, string):
        strLen = len(string)
        if strLen == 1:
            return string
        mapDict = {}
        mapDict[string[0]] = 0
        du = [1 for _ in range(strLen)]
        for i in range(1, strLen):
            if string[i] in mapDict:
                # 举下面的例子， 字符串为abcdebca， 最后一个a重复了， 但是当前坐标减去上一个(第一个)
                # 的差值大于上一个最大不重复子串bc的长度, 所以a是已经不再当前子串里的， 就不算做重复
                # 所以加一
                if i - mapDict[string[i]] > du[i-1]:
                    du[i] = du[i-1] + 1
                else:
                    # 如果是在当前不重复子串里面重复了， 那么当前下标的最大不重复子串就是减去上一个重复的
                    # 比如： abcdebca, 当前值为第二个b， 那么该索引下的最大不重复子串就是cdeb， 长度为
                    # 第二个b的索引减去第一个b的索引。
                    du[i] = i - mapDict[string[i]]
            else:
                du[i] = du[i-1] + 1
            mapDict[string[i]] = i
        # 怎么快速的在无序的数组里面找到最大值， 并且保存下下标
        return max(du)


if __name__ == "__main__":
    s = Solution()
    testString = "abcabcdefghfsdf"
    maxLen = s.maxLenNoRepeatSubStr(testString)
    print("字符串: {}的最大不重复长度为: {}".format(testString, maxLen))

