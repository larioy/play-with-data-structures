# -*- encoding: utf-8 -*-


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return -1
        l = 0
        r = size - 1
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < nums[r]:
                # mid 有可能是最小值
                # [7,8,1,2,3]
                r = mid
            elif nums[mid] > nums[r]:
                # mid 肯定不是最小值
                # [7,8,9,10,11,1,2,3]
                l = mid + 1
            else:
                # 都有可能，所以就把 r 排除了
                # [1,1,1,1,1,0,1]
                assert nums[mid] == nums[r]
                r = r - 1
        return nums[l]


if __name__ == "__main__":
    s = Solution()
    a = s.findMin([3,4,5,1,1,1,2,10,1,5,7,4,5,6,7])
    print(a)


