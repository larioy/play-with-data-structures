# -*- encoding: utf-8 -*-
import random
from collections import defaultdict


class Solution(object):
    # 只会找出重复的数字， 不会找出所有的重复的
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        size = len(nums)
        if size < 2:
            return -1

        # 先统一检查数字是不是越界了, 保证数组里面的数字是在0~n-1之间
        for i in range(size):
            if nums[i] < 0 or nums[i] > size - 1:
                return -1
        repeat_dict = defaultdict(list)
        for i in range(size):
            # nums[i] 应该在 i 的位置上
            while i != nums[i]:
                # 发现要交换的那个数和自己一样，就可以返回了
                if nums[i] == nums[nums[i]]:
                    repeat_dict[nums[i]].append(i)
                    # 直接break， 那么最终数组就不是排序的
                    break
                    # return nums[i]
                self.__swap(nums, i, nums[i])
            print(nums)
        print(repeat_dict)
        return -1

    def __swap(self, nums, index1, index2):
        if index1 == index2:
            return
        temp = nums[index1]
        nums[index1] = nums[index2]
        nums[index2] = temp


class bucketSort(object):
    # 桶排序法， 实现可行， 数组范围内的数都会进行排序
    def _max(self, oldlist):
        _max = oldlist[0]
        for i in oldlist:
            if i > _max:
                _max = i
        return _max

    def _min(self, oldlist):
        _min = oldlist[0]
        for i in oldlist:
            if i < _min:
                _min = i
        return _min

    def sort(self, oldlist):
        _max = self._max(oldlist)
        _min = self._min(oldlist)
        # 生成一个M空桶
        s = [0 for i in range(_min, _max + 1)]
        # 按桶板的大小将填入桶里面, 遍历一次原始长度
        for i in oldlist:
            s[i - _min] += 1
        current = _min
        # 从桶的最小处进行遍历， 重排原始数组
        n = 0   # 原始数组的索引
        for i in s:   # 遍历的次数也是原始列表的长度， for+while
            while i > 0:
                oldlist[n] = current
                i -= 1
                n += 1
            current += 1
        # 将值和重复的次数撸出来
        repeat_num = [{index: value} for index, value in enumerate(s) if value > 1]
        print(repeat_num)

    def __call__(self, oldlist):
        self.sort(oldlist)
        return oldlist


class Bin_Solution:
    # 查找n+1长度的数组里n范围内的重复数字
    def findDuplicate(self, nums):
        """
        【不修改数组找出重复的数字】
        给定一个包含 n + 1 个整数的数组 nums，
        其数字都在 1 到 n 之间（包括 1 和 n），
        可知至少存在一个重复的整数。
        假设只有一个重复的整数，找出这个重复的数。

        不能用于[20,30,90]长度为3， 范围为70的场景
        :type nums: List[int]
        :rtype: int
        """
        left = 1      # 注意初值为1
        right = len(nums) - 1    # right只取到n的，不是n+1
        while left < right:
            # 取中点有两种方式，偏左和偏右
            mid = left + (right - left + 1) // 2  # 4
            count = 0
            for num in nums:
                if num < mid:
                    count += 1
            if count < mid:
                # 比 4 小的个数，最多就只能是 3
                # 所以重复的肯定不是 [1,2,3]，不能排除 4
                # 因为左边不变，所以取中点的时候，就要偏右
                left = mid
            else:
                # 比 4 小的个数，达到 4 或者更多
                # 重复的就落在 [1,2,3]
                right = mid - 1
        # 跳出循环肯定是因为 start = end
        return left


if '__main__' == __name__:
    test_array = [2, 6, 3, 8, 5, 1, 1, 9, 1, 0, 9]
    example = Solution()
    res = example.duplicateInArray(test_array)
    print(res)
    a = [1, 1, 1, 5, 3, 2, 9, 4, 0]
    bucketSort()(a)
    print(a)

    bs = Bin_Solution()
    n_1 = [10, 20, 30, 40, 50, 60, 90, 20, 70]
    print(bs.findDuplicate(n_1))
