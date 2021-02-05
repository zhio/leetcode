#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        isPirme = [1] * n
        for i in range(2,n):
            if isPirme[i] == 1:
                res += 1
                if (i*i<n):
                    j = i * i 
                    while j < n:
                        isPirme[j] = 0
                        j += i
        return res
# @lc code=end

