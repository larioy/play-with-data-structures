# -*- encoding: utf-8 -*-

class Solution(object):

    def reversePairs(self, arr):
        if len(arr) <= 1:
            return 0
        listLen = len(arr)
        rPairs = self.gbSort(arr, 0, listLen-1)
        return rPairs

    def gbSort(self, arr, left, right):
            if left >= right:
                return 0
            mid = left + (right-left)//2
            leftParis = self.gbSort(arr, left, mid)
            rightParis = self.gbSort(arr, mid+1, right)
            mergeParis = 0
            if arr[mid] > arr[mid+1]:
                mergeParis = self.merge(arr, left, mid, right)

            return leftParis + rightParis + mergeParis

    def merge(self, arr, left, mid, right):
        temp = [num for num in arr]  # 需要一个和原数组一样大小的空间， 可以传入，避免不断的申请释放
        # 复制临时区间
        l = left
        r = mid + 1    # 这里的起点最开始弄错了，
        res = 0
        for k in range(left, right+1):
            if l > mid:
                arr[k] = temp[r]
                r += 1
            elif r > right:
                arr[k] = temp[l]
                l += 1
            elif temp[l] <= temp[r]:
                arr[k] = temp[l]
                l += 1
            else:
                assert temp[l] > temp[r]
                arr[k] = temp[r]
                r += 1
                # 这里的场景就是连个有序数组在进行归并的过程中有
                # [7, 8, 9], [2, 4, 6], 左边的数组比右边当前索引对应的值大，
                # 关键点是左边和右边的数组都是有序的， 如果左边数组的当前数比右边的当前数大
                # 那么左边数组的当前值的右侧一定比右侧数组的当前值大
                # 例子为: 左边当前值为7， 右边为2， 那么左边的8,9就一定比2大
                res += mid - l + 1
        return res


if __name__ == "__main__":
    s = Solution()
    arr = [1,2,3,4,5,6,0]
    res = s.reversePairs(arr)
    print("数组: {}一共有{}个逆序对".format(arr, res))
