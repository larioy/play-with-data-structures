# -*- encoding: utf-8 -*-


class Solution(object):

    def insertSort(self, arr):
        lLen = len(arr)
        if lLen <= 1:
            return arr
        for i in range(0, lLen):
            current = arr[i]
            minIndex = i
            for j in range(lLen-1, i, -1):
                if arr[j] < current:
                    current = arr[j]
                    minIndex = j
            arr[minIndex], arr[i] = arr[i], arr[minIndex]
        return arr


if __name__ == "__main__":
    s = Solution()
    arr = [5, 8, 1, 0, 2, 7, 3, 9, 4, 6, 9, 1, 1]
    s.insertSort(arr)
    print("排序后的数组为:{}".format(arr))


