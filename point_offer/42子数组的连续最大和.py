# -*- encoding: utf-8 -*-

"""
解题思路：
1、保证连续和获取连续的子数组的最大值如下：
如果前一个数的子数组和为小于0的，那么对当前数的累加和是有害的， 那么当前值的累加和为自己，连续的子数组就是从自己开始

2、动态的更新最大子数组连续和，

"""


class Solution(object):
    def orderMaxSum(self, order):
        if len(order) == 0:
            return None
        if len(order) == 1:
            return order[0]

        preSum = order[0]
        maxSum = order[0]
        for i in range(1, len(order)):
            if preSum < 0:
                preSum = order[i]
            else:
                preSum += order[i]
            maxSum = max(preSum, maxSum)

        return maxSum


if __name__ == "__main__":
    s = Solution()
    order = [1, -2, 3, 10, -4, 7, 2, -5]
    maxSum = s.orderMaxSum(order)
    print("数组:{}的最大连续子数组和为: {}".format(order, maxSum))
