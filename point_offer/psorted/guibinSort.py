# -*- encoding: utf-8 -*-


class Solution(object):
    temp = []

    def gbSort(self, arr, l, r):
        if l > r or len(arr) == 0 or l > len(arr):
            return -1
        if l >= r:
            return
        if len(arr) == 1:
            return arr

        mid = l + (r-l)//2
        self.gbSort(arr, l, mid)
        self.gbSort(arr, mid+1, r)
        if arr[mid] > arr[mid+1]:
            self.merge(arr, l, r)

    def merge(self, arr, l, r):
        self.temp = [num for num in arr]

        mid = l + (r-l)//2
        left = l
        right = mid + 1
        for k in range(l, r+1):
            if left > mid:
                arr[k] = self.temp[right]
                right += 1
            elif right > r:
                arr[k] = self.temp[left]
                left += 1
            elif self.temp[left] > self.temp[right]:
                arr[k] = self.temp[right]
                right += 1    # 这里是先交换后加一
            else:
                arr[k] = self.temp[left]
                left += 1


if __name__ == "__main__":
    s = Solution()
    arr = [5, 8, 1, 0, 2, 7, 3, 4, 6, 9, 9, 0, 0, 1]
    left = 0
    right = len(arr) - 1
    s.gbSort(arr, left, right)
    print("归并排序后的数组为:{}".format(arr))