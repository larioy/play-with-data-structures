# -*- encoding: utf-8 -*-


class Solution(object):
    def SquareCover(self, n):
        a = 1
        b = 2
        for i in range(3, n+1):
            c = a + b
            a = b
            b = c

        a = 1
        b = 2
        while n-1:     # 因为不是从0开始的所以为n-1
            d = a + b
            a = b
            b = d
            n = n - 1
        return c, a


if __name__ == "__main__":
    s = Solution()
    print(s.SquareCover(12))
