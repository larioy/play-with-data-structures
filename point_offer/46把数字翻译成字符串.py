# -*- encoding: utf-8 -*-


class Solution(object):

    def translatArrtoStr(self, arr):
        for i in range(len(arr)):
            if int(i) not in range(10):
                return -1
        du = [1 for _ in arr]
        if 10 <= int(arr[0:2]) <= 25:
            du[1] = 2
        else:
            du[1] = 1
        arrLen = len(arr)
        for i in range(2, arrLen):
            if 10 <= int(arr[i-1])*10 + int(arr[i]) <= 25:  # 这种方式也可以将01转换为1的
                du[i] = du[i-1] + du[i-2]
            else:
                du[i] = du[i-1]
                # 注意这里并不需要加一， 因为最后一个数字不能和前面的结合， 那总数就是前一个的总数
        return du[arrLen-1]


if __name__ == "__main__":
    s = Solution()
    arr = "12258"
    count = s.translatArrtoStr(arr)
    print(count)

