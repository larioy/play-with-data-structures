# -*- encoding: utf-8 -*-

"""
分析题解：
0-9数字： 一共9位
10-99数字： 一共（99-10+1）* 2 为180位      2为数字的位数
100-999数字： 一共(999-100+1) * 3 为2700位    3为数字的位数

比如： 第1000个位为  （1000-9-180) < 2700, 所以第1000位为3位数的
(1000-9-180)//3 == 270 (1000-9-180) % 3 == 1,
所以第1000位为第370数字之后的371，余1， 所以第1000为3
"""

class Solution(object):
    def getNumKkey(self, k):
        base = 9
        count = 1
        while k - base*count > 0:
            k = k - base*count
            base = base*10
            count += 1

        # lastStep为最长位数区间段
        lastStep = k
        bitAdjust = lastStep % count
        if bitAdjust == 0:   # 正好整除说明正好是完整的count的数
            realNum = 10**(count-1) + lastStep//count - 1   # 因为从0开始计数
            return realNum % 10
        else:
            # 因为存在余数， 所以实际的数为未完成的。 所以不用再减一
            realNum = 10**(count-1) + lastStep//count
            print(realNum)
            # 第1000位的除以3余1, 前一个完整的数为370(见文件开始分析)， 那么下一个为371的百位，
            # 所以有下面的循环
            for i in range(bitAdjust, count):
                realNum = realNum//10
            return realNum%10


if __name__ == "__main__":
    s = Solution()
    print(s.getNumKkey(1000))
