# -*- encoding: utf-8 -*-

"""
求机器人的运动范围: 机器人的运动的范围限制为坐标位数的和要小于多少多少
思路： 使用队列做广度优先遍历
标记的时候在进入队列的时候。
"""

class Solution(object):
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def posSum(self, row, col):
        res = 0
        while row:
            res += row % 10
            row = row // 10
        while col:
            res += col % 10
            col = col // 10
        return res

    def getArea(self, rows, cols, k):
        marked = [[False for _ in range(cols)] for _ in range(rows)]
        queue = [(0, 0)]
        res = 0
        while queue:
            row, col = queue.pop(0)
            for direction in self.directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if 0 <= new_col < cols and 0 <= new_row < rows and \
                    self.posSum(new_row, new_col) <= k and not marked[new_row][new_col]:
                    marked[new_row][new_col] = True
                    queue.append((new_row, new_col))
                    res += 1
        return res, marked


if __name__ == "__main__":
    s = Solution()
    count, marked = s.getArea(10, 12, 10)
    print(count)
    for i in range(len(marked)):
        print(marked[i])

