# -*- encoding: utf-8 -*-


def getRepeatNumHash(arr):
    """
    通过hash过滤重复额数字
    特点： 可以返回所有的重复的数字
    :param arr:
    :return:
    """
    num_dict = {}
    for num in arr:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    repeatNum = [num for num in num_dict if num_dict[num] > 1]
    return repeatNum


def getRepeatNumHash1(arr):
    """
    通过桶排序的方式获取第一个重复的数字
    前提： 在1-n个数字里面只有一个重复的数字
    :param arr:
    :return:
    """
    if len(arr) < 1:
        return -1

    length = len(arr)
    for i in arr:
        if i < 0 or i > length:
            print("给出的数组不符合要求， 其中的数字超出范围了")
            return

    for i in arr:
        while i != arr[i]:
            if arr[i] == arr[arr[i]]:
                print("第一个重复的数字为: {}".format(arr[i]))
                return
            swap(arr, i, arr[i])


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]



def binarySearch(arr):
    """
    要求： 长度为n+1的数组的数范围为[1,n], 里面有重复的数字. 注意这里是从1开始
    :param arr:
    :return:
    """
    lLen = len(arr)
    l = 1
    r = lLen - 1
    while l < r:
        mid = l + (r-l+1)//2  # 为什么要偏左
        count = 0
        for num in arr:
            if num < mid:
                count += 1
        if count < mid:
            l = mid
        else:
            r = mid - 1
    return l


if __name__ == "__main__":
    test_arr = [1, 2, 3, 4, 5, 7, 7, 8, 8, 1]
    print(getRepeatNumHash(test_arr))

    """
    在1-n的数组里面，数组里的数都只会在1-n里面， 找出数组里面的重复的第一个数
    """
    test_arr = [1, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10]
    getRepeatNumHash1(test_arr)


"""
桶排序怎么实现重复数字的排序， [1, 2, 3, 3, 4, 5, 6]   ？
桶排序是只能实现连续的数字之间的排序的吗？  
[100, 101, 102, 103, 104, 105]  可以
[100, 200, 201, 233, 300, 400]  可以吗？

"""
