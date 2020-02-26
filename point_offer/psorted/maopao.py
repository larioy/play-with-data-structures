# -*- encoding: utf-8 -*-


class Solution(object):

    def maopao(self, arr):
        lLen = len(arr)
        if lLen <= 1:
            return arr
        for i in range(lLen-1, 0, -1):
            for j in range(i):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    s = Solution()
    arr = [5, 8, 1, 0, 2, 7, 3, 9, 4, 6, 9, 1, 1]
    s.maopao(arr)
    print("数组排序后为: {}".format(arr))
