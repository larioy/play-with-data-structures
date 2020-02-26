# -*- encoding: utf-8 -*-

def getNumFromArr(arr, num):
    """
    在一个从右比左大， 下比上大的二维数组中找一个数。 注意： 新行第一个数不一定比上一行的最后一个数大
    :param arr: 二维数组
    :param num:
    :return:
    """
    rows = len(arr)
    cols = len(arr[0])
    row = 0
    col = cols - 1
    while 0 <= row < rows and 0 <= col < cols:
        if num > arr[row][col]:
            row += 1

        if num < arr[row][col]:
            col -= 1
        print("找到了")
        return True


def getNumFromArrByBinary(arr, num):
    """
    通过二分法进行查找, 逻辑暂时没懂。为什么行的列里面是小于等于， 行是大于等于
    注意这里的两个边界
    最左边一个小于等于, mid的边界判断条件, r与l的取值
    最右边一个大于等于, mid的边界判断条件, r与l的取值
    :param arr:
    :param num:
    :return:
    """
    rows = len(arr)
    cols = len(arr[0])

    row = 0
    col = cols - 1
    while col >= 0 and row < rows:
        if col == 0 and arr[row][0] > num:
            return False
        l = 0
        r = col
        while l < r:
            mid = l + (r - l + 1)//2
            if arr[row][mid] <= num:
                l = mid
            else:
                r = mid - 1
        # 这里要注意
        col = l

        if row == rows - 1 and arr[rows-1][col] < num:
            return False

        l = row
        r = rows - 1
        while l < r:
            mid = l + (r - l)//2
            if arr[mid][col] >= num:
                r = mid
            else:
                l = mid + 1

        row = l

        if arr[row][col] == num:
            print("找到了{}".format(num))
            return True


def getNumFromArr1(arr, num):
    """
    找的是之字形的单调递增的二维数组
    :param arr:
    :param num:
    :return:
    """
    rows = len(arr)
    cols = len(arr[0])

    l = 0
    r = rows * cols - 1
    while l < r:
        mid = l + (r - l)//2
        if arr[mid//rows][mid%cols] > num:
            r = mid - 1    # 为啥是这样
        elif arr[mid//rows][mid%cols] < num:
            l = mid + 1    # 为啥是这样
        else:
            print("找到了")
    return -1


if __name__ == "__main__":
    arr = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    getNumFromArr(arr, 7)
    getNumFromArrByBinary(arr, 7)
