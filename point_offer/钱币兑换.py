# -*- encoding: utf-8 -*-


class Solution(object):
     def changeMoney(self, total, mini, media, maxi):
         if total < mini:
             return -1
         miniCount = total//mini
         mediaCount = total//media
         maxiCount = total//maxi
         for i in range(0, miniCount+1):
             for j in range(0, mediaCount+1):
                 for k in range(0, maxiCount+1):
                     if mini*i+media*j+maxi*k == total:
                         print("{}:{}张， {}:{}张, {}:{}张".format(mini, i, media, j, maxi, k))
                     if mini*i+media*j+maxi*k > total:
                         break


if __name__ == "__main__":
    s = Solution()
    total, mini, media, maxi = 100, 2, 5, 10
    s.changeMoney(total, mini, media, maxi)

