# -*- encoding: utf-8 -*-

"""
变态跳台阶： 有n机台阶， 每一次可以跳1-n， 问一共有多少中跳法。
依然采用从尾到前的推理， 第i级台阶， 最后一步可以为1~i, 第i-1的台阶有1~i-1种跳法
所以每一个i级台阶的跳法都要累积之前的不同跳法
"""


class Solution(object):
    def JumpStep(self, n):
        du = [1 for _ in range(n+1)]     # 注意这里的范围是什么，[1, n]闭区间
        du[0] = 0
        du[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):  # 注意这个边界是[1, i-1]
                du[i] = du[i] + du[j]
        return du[n]


if __name__ == "__main__":
    s = Solution()
    print(s.JumpStep(12))
