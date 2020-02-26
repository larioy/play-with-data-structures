# -*- encoding: utf-8 -*-


class Solution(object):
    def getSingleNum(self, arr):
        lLen = len(arr)
        if lLen < 2:
            return -1
        xor = 0
        for num in arr:
            xor ^= num
        bitOne = 0
        while xor & 1 == 0:
            xor >>= 1
            bitOne += 1
        res = [0, 0]
        for num in arr:
            if (num >> bitOne) & 1:
                res[0] ^= num
            else:
                res[1] ^= num
        return res


if __name__ == "__main__":
    s = Solution()
    arr = [10, 20, 3, 3, 4, 4]
    res = s.getSingleNum(arr)
    print("数组: {}中的两个单数为: {}".format(arr, res))
