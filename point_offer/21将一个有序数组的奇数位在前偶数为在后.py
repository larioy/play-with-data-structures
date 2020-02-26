# -*- encoding: utf-8 -*-
"""
将一个有序的数组调整为奇数在前偶数在后， 并且要保证奇数部分和偶数部分分别是有序的
注意这是一个有序的数组

"""


class Solution(object):
    def adjustOdd(self, arr):
        l = 0
        r = len(arr) - 1
        while True:
            while r >= l and arr[r] & 1 == 0:
                r -= 1
            while l <= r and arr[l] & 1 == 1:
                l += 1

            if l > r:
                break
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        # 最后排完序后再对左边的奇数部分进行排序， 对右边的偶数部分进行排序
        self.gbSort(arr, 0, l)
        self.gbSort(arr, l, len(arr)-1)
        return arr

    def gbSort(self, arr, left, right):
            if left >= right:
                return 0
            mid = left + (right-left)//2
            self.gbSort(arr, left, mid)
            self.gbSort(arr, mid+1, right)
            if arr[mid] > arr[mid+1]:
                self.merge(arr, left, mid, right)

    def merge(self, arr, left, mid, right):
        temp = [num for num in arr]  # 需要一个和原数组一样大小的空间， 可以传入，避免不断的申请释放
        # 复制临时区间
        l = left
        r = mid + 1    # 这里的起点最开始弄错了，
        for k in range(left, right+1):
            if l > mid:
                arr[k] = temp[r]
                r += 1
            elif r > right:
                arr[k] = temp[l]
                l += 1
            elif temp[l] <= temp[r]:   # 注意这里比较使用的是进入函数前的数组，也就是temp
                arr[k] = temp[l]
                l += 1
            else:
                assert temp[l] > temp[r]
                arr[k] = temp[r]
                r += 1



if __name__ == "__main__":
    s = Solution()
    print(s.adjustOdd([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))

    arr = [3,6,1,9,2,7,5,8,4]
    s.gbSort(arr, 0, len(arr)-1)
    print(arr)