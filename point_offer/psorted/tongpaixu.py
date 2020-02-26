# -*- encoding: utf-8 -*-


class Solution(object):

    def tongpaiSort(self, arr):
        lLen = len(arr)
        if lLen <= 1:
            return
        for i in range(len(arr)):
            while arr[i] != i:
                arr[i], i = i, arr[i]


if __name__ == "__main__":
    s = Solution()
    arr = [1, 7, 2, 0, 3, 9, 8, 5, 4, 6]
    s.tongpaiSort(arr)
    print("排序后的数组为:{}".format(arr))
