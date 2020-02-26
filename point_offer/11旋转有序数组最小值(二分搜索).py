# -*- encoding: utf-8 -*-


class Solution(object):
    def getMin(self, arr):
        size = len(arr)
        if size == 1:
            return arr[0]
        if size == 0:
            return -1

        l = 0
        r = size - 1
        while l < r:
            mid = l + (r -l)//2
            if arr[mid] > arr[r]:
                l = mid + 1
            elif arr[mid] < arr[r]:
                r = mid
            else:
                r = r - 1
        return arr[l]


if __name__ == "__main__":
    s = Solution()
    arr = [3, 4, 5, 1, 2]
    print(s.getMin(arr))

    arr = [1, 1, 1, 0, 1]
    print(s.getMin(arr))





