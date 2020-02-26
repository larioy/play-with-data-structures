# -*- encoding: utf-8 -*-


class Solution(object):
    def orderSqure(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        res = []
        bottom, top, left, right = rows-1, 0, 0, cols-1
        while top <= bottom and left <= right:
            for col in range(left, right):
                res.append(matrix[top][col])
            for row in range(top, bottom+1):    # 注意转角的边界
                res.append(matrix[row][right])
            if left != right:
                for col in range(left, right)[::-1]:
                    res.append(matrix[bottom][col])
            if top != bottom:
                for row in range(top+1, bottom)[::-1]:   # 注意这里的边界top+1
                    res.append(matrix[row][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res

    def createSqure(self, rows, cols, base, interval=0):
        matrix = [[base for _ in range(cols)] for _ in range(rows)]
        count = 0
        bottom, top, left, right = rows-1, 0, 0, cols-1
        while top <= bottom and left <= right:
            for col in range(left, right):
                matrix[top][col] += count
                count += 1 + interval
            for row in range(top, bottom+1):
                matrix[row][right] += count
                count += 1 + interval
            if left != right:
                for col in range(left, right)[::-1]:
                    matrix[bottom][col] += count
                    count += 1 + interval
            if top != bottom:
                for row in range(top+1, bottom)[::-1]:
                    matrix[row][left] += count
                    count += 1 + interval
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return matrix


if __name__ == "__main__":
    s = Solution()
    matrix = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]
    ]
    res = s.orderSqure(matrix)
    print("顺序打印后的二维矩阵为: {}".format(res))

    matrix = s.createSqure(4, 4, 1)
    print("按顺时针创建的二维矩阵为: {}".format(s.orderSqure(matrix)))

    matrix = s.createSqure(6, 6, 1)
    print("按顺时针创建的二维矩阵为: {}".format(s.orderSqure(matrix)))


