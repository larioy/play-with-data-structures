# -*- encoding: utf-8 -*-


class Solution(object):

    def findNumCount(self, arr, num):
        lLen = len(arr)
        if lLen == 0:
            return -1
        if lLen == 1 and num != arr[0]:
            return -1
        if lLen == 1 and num == arr[0]:
            return 1
        # 确定查找的数是在范围内的， 否则查询会进入死循环
        if num < arr[0] or num > arr[-1]:
            return 0
        maxIndex = self.getMaxEquilIndex(arr, num)
        minIndex = self.getMinEquilIndex(arr, num)
        if maxIndex == -1:
            return 0
        else:
            return maxIndex-minIndex+1

    def getMinEquilIndex(self, arr, num):
        """
        不能找比数组最小值还小的数
        :param arr:
        :param num:
        :return:
        """
        if arr == 0:
            return -1
        if len(arr) == 1:
            return arr[0]
        l = 0
        r = len(arr) - 1
        while l < r:
            mid = l + (r-l)//2
            if arr[mid] >= num:
                r = mid
            else:
                l = mid + 1
        return l

    def getMaxEquilIndex(self, arr, num):
        """
        不能找比数组大的数
        :param arr:
        :param num:
        :return:
        """
        if arr == 0:
            return -1
        if len(arr) == 1:
            return arr[0]
        l = 0
        r = len(arr) - 1
        while l < r:
            mid = l + (r-l+1)//2   # 增加1可以找比有序数组最大数大的值
            if arr[mid] <= num:
                l = mid
            else:
                r = mid - 1
        return l


if __name__ == "__main__":
    s = Solution()
    arr = [1, 2, 3, 3, 3, 3, 4, 5]
    num = 3
    index = s.getMaxEquilIndex(arr, num)
    print("在数组:{}中, 大于等于{}的边界索引为:{}".format(arr, num, index))

    index = s.getMinEquilIndex(arr, num)
    print("在数组:{}中, 小于等于{}的边界索引为:{}".format(arr, num, index))

    num = 0
    count = s.findNumCount(arr, num)
    print("在数组: {}中, 数{}的个数为:{}".format(arr, num, count))
