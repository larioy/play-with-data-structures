# -*- encoding: utf-8 -*-


class Solution(object):

    def quickSort(self, arr):
        """
        支持重复数的快速排序
        易错点： 不能有>=或<=的if条件， 否则或出现死循环， 递归跳不出来
        :param arr:
        :return:
        """
        lLen = len(arr)
        if lLen <= 1:
            return arr
        current = arr[0]
        little = []
        great = []
        equil = []
        for num in arr:
            if num < current:
                little.append(num)
            elif num > current:
                great.append(num)
            else:
                equil.append(num)
        return self.quickSort(little) + equil + self.quickSort(great)


if __name__ == "__main__":
    s = Solution()
    arr = [5, 8, 1, 0, 2, 7, 3, 4, 6, 9, 9, 0, 0, 1]
    newarr = s.quickSort(arr)
    print("排序后的数组为:{}".format(newarr))
