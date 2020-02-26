# -*- encoding: utf-8 -*-


class Solution(object):
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def findPath(self, arr, substr):
        """
        矩阵中找路径
        任意一个起点： 说明是要遍历到矩阵里面的所有节点的，所以双重for
        因为为路径中找到字符串： 所以是深度优先搜索
        因为不能走走过的， 所以需要进行标记
        路径的判断注意字符串索引index的维护
        :param arr:
        :param substr:
        :return:
        """
        rows = len(arr)
        cols = len(arr[0])
        marked = [[0 for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                # 最开始的索引为0
                if self._hasPath(arr, substr, 0, row, col, marked, rows, cols):
                    return True
        # 如果所有的点都走完了， 那么就返回失败
        return False

    def _hasPath(self, arr, substr, index, row, col, marked, rows, cols):
        # 判断字符的索引是否达到了最后的一个
        if index == len(substr) - 1:
            if arr[row][col] == substr[-1]:
                return True

        # 判断当前的二维数组的位置是否和字符串index索引值相等， 相等的话才能继续下一个目标
        if arr[row][col] == substr[index]:
            # 先占位标记这个坐标是被走过了
            marked[row][col] = 1
            for direction in self.directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if 0 <= new_col < cols and 0 <= new_row < rows and not marked[new_row][new_col] \
                    and self._hasPath(arr, substr, index+1, new_row, new_col, marked, rows, cols):
                    return True
            # 如果for循环内没有一直走到底的话， 说明这个坐标行不通， 解除占座
            marked[row][col] = 0
        return False


if __name__ == "__main__":
    matrix = [
        ["A", "B", "C", "E"],
        ["S", "F", "E", "S"],
        ["A", "D", "E", "E"]
    ]
    s = Solution()
    str1 = "ABCEFSADEESE"
    print(s.findPath(matrix, str1))

    str1 = "FDE"
    print(s.findPath(matrix, str1))

"""
怎么找出所有符合要求的路径， 即所有路径？
怎么找出所有的符合要求的路径， 包含坐标的走向呢？

"""