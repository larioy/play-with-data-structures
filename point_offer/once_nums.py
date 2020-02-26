# -*- encoding: utf-8 -*-


class Solution(object):
    def findNumsAppearOnce(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        if l < 2:
            raise Exception('程序出错')
        if l == 2:
            return nums

        # 全部亦或一遍
        xor = 0
        for num in nums:
            xor ^= num

        # 最末尾的 1 从右向左边数在第几位
        counter = 0
        while xor & 1 == 0:
            xor >>= 1
            counter += 1

        res = [0, 0]
        for num in nums:
            if (num >> counter) & 1 == 1:
                res[1] ^= num
            else:
                res[0] ^= num
        return res


class Solution1:
    def maxInWindows(self, num, size):
        # write code here
        # 存放可能是最大值的下标
        maxqueue = []
        # 存放窗口中最大值
        maxlist = []
        n = len(num)
        # 参数检验
        if n == 0 or size == 0 or size > n:
            return maxlist
        for i in range(n):
            # 判断队首下标对应的元素是否已经滑出窗口
            if len(maxqueue) > 0 and i - size >= maxqueue[0]:
                maxqueue.pop(0)
            while len(maxqueue) > 0 and num[i] > num[maxqueue[-1]]:
                maxqueue.pop()
            maxqueue.append(i)
            if i >= size - 1:
                maxlist.append(num[maxqueue[0]])
        return maxlist


class Solution2(object):
    def isContinuous(self, numbers):
        """
        :type numbers: List[int]
        :rtype: bool
        """
        size = len(numbers)
        if size != 5:
            return False
        # 最小值和最大值都设置成一个不可能取到的值
        min_val = 14
        max_val = -1

        flag = 0
        for num in numbers:
            if not 0 <= num <= 13:
                return False
            if num == 0:
                continue
            # 右移：看看这一位是不是用过了, 用过了就一定不会构成顺子
            if (flag >> num) & 1 == 1:
                return False

            # 左移：表示这一位我现在要占用
            flag = flag | (1 << num)

            min_val = min(min_val, num)
            max_val = max(max_val, num)
            if max_val - min_val >= 5:
                return False
        return True


if __name__ == "__main__":
    arr = [3, 3, 4, 4, 50000, 6]
    s = Solution()
    print(s.findNumsAppearOnce(arr))

    arr = [1,2,3,4,5,6,100,2,30,80,40,20]
    s = Solution1()
    print(s.maxInWindows(arr, 3))


    arr = [1,2,3,3,6]
    s2 = Solution2()
    print(s2.isContinuous(arr))
