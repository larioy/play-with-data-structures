# -*- encoding: utf-8 -*-


class Solution:
    def verifySquenceOfBST(self, sequence):
        """
        :type sequence: List[int]
        :rtype: bool
        """
        # 先写特殊情况
        l = len(sequence)
        if l == 0:
            return False
        if l == 1:
            return True

        return self.__helper(sequence, 0, l - 1)

    def __helper(self, sequence, left, right):
        # 先写递归终止条件
        if left >= right:
            return True
        # 此时区间最右边的数作为标定元素
        pivot = sequence[right]
        # 设置一个遍历指针，把 [left, right -1] 这个区间里的元素全部看一遍

        # 正确的情况是：最右边的元素把前面的数组分成两部分：
        # 第 1 部分的元素全部严格小于最右边的元素
        # 第 2 部分的元素全部严格大于最右边的元素
        point = left
        while sequence[point] < pivot:
            point += 1
        # 此时 [left, point - 1] 中的元素都严格比最右边的元素小
        # 下面就依次验证后面的元素是不是都严格比最右边的元素大就好了
        mid = point - 1
        # 此后，所有的数都应该比 pivot 大
        while point < right:
            if sequence[point] > pivot:
                point += 1
            else:
                return False
        return self.__helper(sequence, left, mid) and self.__helper(sequence, mid + 1, right - 1)


if __name__ == "__main__":
    s = Solution()
    # postorder = [10, 5, 15, 2, 7, 12, 17]
    # postorder = [2, 7, 5, 12, 17, 15, 10]
    postorder = [7, 6, 5, 4, 3, 2, 1]
    print("数组{}构成一个二叉树的后续: {}".format(postorder, s.verifySquenceOfBST(postorder)))