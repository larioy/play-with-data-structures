# -*- encoding: utf-8 -*-


class Solution(object):

    def reverseStr(self, string):
        sLen = len(string)
        if sLen < 2:
            return string
        string = list(string)
        self._reverse(string, 0, sLen-1)
        l = 0
        for i in range(sLen):
            if string[i] == ' ':
                self._reverse(string, l, i-1)
                l = i+1    # 如果当前是分隔符， 那么下一个单词的开始一定是从下一个开始的。
            else:
                i += 1
        self._reverse(string, l, sLen-1)
        string = ''.join(string)
        return string

    def _reverse(self, string, l, r):
        sLen = len(string)
        if sLen < 2:
            return string
        while l < r:
            string[l], string[r] = string[r], string[l]
            l += 1
            r -= 1
        return string


if __name__ == "__main__":
    s = Solution()
    string = "  hello python.  "
    print(s.reverseStr(string))



