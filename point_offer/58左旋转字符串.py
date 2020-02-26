# -*- encoding: utf-8 -*-


class Solution(object):

    def leftReverseStr(self, string, n):
        sLen = len(string)
        if sLen < 1 or n > sLen or n < 0:
            return -1
        string = list(string)
        self._reverse(string, 0, sLen-1)
        self._reverse(string, 0, sLen-1-n)
        self._reverse(string, sLen-n, sLen-1)
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
    testString = "abcdefgh"
    num = 4
    string = s.leftReverseStr(testString, num)
    print("字符串:{}左旋{}个字符后的新字符串为: {}".format(testString, num, string))
