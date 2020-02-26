# -*- encoding: utf-8 -*-


"""
剪绳子： 同样使用从尾到前进行推导， 一刀剪下去剪成n和length-n, 那么这种剪法的最大值要么du[length]本身
要么为n*(length-n), 要么为n*du[length-n], 其中length-n为长度为length-n的最大值.

然后每一个长度都这么剪， 于是就有了循环取最大值

"""


class Solution(object):
    def cutTie(self, length):
        if length == 1:
            return 1
        du = [i for i in range(length+1)]  # 设置初值最重要
        for i in range(1, length+1):
            for j in range(1, i):
                du[i] = max(du[i], j*(i-j), j*du[i-j])
        return du[length]


if __name__ == "__main__":
    s = Solution()
    print(s.cutTie(20))
