# -*- encoding: utf-8 -*-

"""
参考网上分析
第一点： 维护一个滑动窗口想到的数据结构为队列， 因为为维护窗口大小， 所以队列里的元素为被测试数组索引
第二点： 维护每一次判断当期索引下的滑动窗口的最大值。  注意： 最大值保存在最大值队列的头部windowsMaxList
        维护方式为： 将当前索引对应的数组值和滑动窗口的所有值比较，弹出滑动窗口中比当前值小的元素
注意点： 因为当前值是比较后才是放入队列里的， 所以要满足len(maxQueue)>0
        另外当前滑动窗口的最大值比较的顺序也是从后向前的(while处)

"""


class Solution(object):

    def getWindowsMax(self, arr, size):
        lLen = len(arr)
        if size < 0 or lLen == 0 or size > lLen:
            return -1
        maxqueue = [0]    # 用于存储滑动窗口的索引, 维护滑动窗口
        windowMaxList = []
        for i in range(lLen):
            # 用于维护滑动窗口的大小， 当窗口过大时就要弹出窗口的最左侧元素
            if len(maxqueue) and i - size >= maxqueue[0]:
                maxqueue.pop(0)
            # 用于寻找当前滑动窗口的最大值， 并且保证最大值为队列的第一个元素
            while len(maxqueue) > 0 and arr[i] > arr[maxqueue[-1]]:
                maxqueue.pop()
            maxqueue.append(i)
            if i - size + 1 >= 0:
                windowMaxList.append(arr[maxqueue[0]])
        return windowMaxList


if __name__ == "__main__":
    windowsArr = [2, 3, 4, 2, 6, 2, 5, 1]
    s = Solution()
    size = 3
    windowsMax = s.getWindowsMax(windowsArr, size)
    print("数组:{}以{}大小为滑动窗口的最大值列表为{}".format(windowsArr, size, windowsMax))



