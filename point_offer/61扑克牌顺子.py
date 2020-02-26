# -*- encoding: utf-8 -*-

"""
整体思路： 因为牌的顺序是在0-13， 可以使用二进制的数来标记位
第一部分： 将牌进行占位
第一点： 0可以充当任何数， 那么遇到0的就跳过
第二点： 使用位运算异或判断是否有重复， 有重复肯定不构成顺子。

第二部分：获取牌的最大最小值差
第一点： 定位到牌的最小值位
第二点： 定位待牌的最大值位，
第三点： 最大值位与最小值差不能>=牌的长度

"""

class Solution(object):
    def isOrder(self, arr):
        lLen = len(arr)
        if lLen < 1:
            return -1
        if lLen == 1:
            return True
        for i in arr:
            if i < 0 or i > 13:
                return -1
        xor = 0
        for num in arr:
            if num == 0:
                continue
            temp = 1 << num
            temp ^= xor
            if not temp:
                return False
            else:
                xor += 1 << num
        # 找到最小的牌(非0),
        while xor & 1 != 1:
            xor = xor >> 1
        # 记录从最小位到最大位的差距
        orderBit = 1
        xor = xor >> 1     # 那掉最低位
        while xor:
            xor = xor >> 1
            orderBit += 1
        if orderBit >= lLen:
            return False
        else:
            return True


if __name__ == "__main__":
    s = Solution()
    orderList = [0, 1, 2, 3, 4]
    print("数组: {}, 判定顺子的结果为: {}".format(orderList, s.isOrder(orderList)))

    orderList = [0, 1, 2, 3, 3]
    print("数组: {}, 判定顺子的结果为: {}".format(orderList, s.isOrder(orderList)))

    orderList = [0, 1, 0, 0, 2]
    print("数组: {}, 判定顺子的结果为: {}".format(orderList, s.isOrder(orderList)))


"""
待丰富:
1、将构成的顺子返回回去
2、添加其他的牌， 除代表自己也可以代表其他， 然后重新判断顺子

"""

