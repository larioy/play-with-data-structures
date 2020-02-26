# -*- encoding: utf-8 -*-

"""
注意最大值的前提是， 只能从下或者从右走， 其他的场景可以类比
注意边界： 全走第一排， 全走最左边一排

"""


class Solution(object):
    def maxSum(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        du = [num for num in matrix[0]]   # 不能这样赋值， 会同步修改原二维数组的第一个元素值的
        # 从第一行开始，假设礼物的最大值走的路径是第一行。 又叫初始最大值
        for i in range(1, cols):
            du[i] = matrix[0][i] + du[i-1]   #
        for row in range(1, rows):
            for col in range(cols):
                # 保证最大值的路径为竖直向下存在
                if col == 0:
                    du[col] = matrix[row][0] + du[0]
                else:
                    # 动态规划， 当前的位置的最大值， 要么从左边来， 要么从上面来
                    # du[col-1]是左边， du[col]是上一个行的， 还没更新到， 所以代表上面(上一行)
                    du[col] = max(du[col], du[col-1]) + matrix[row][col]

        return max(du)


if __name__ == "__main__":
    matrix = [
                [2, 3, 1],
                [1, 7, 1],
                [4, 6, 1]
            ]

    s = Solution()
    maxVal = s.maxSum(matrix)
    print("二维数组:{}的礼物的最大值为{}".format(matrix, maxVal))
