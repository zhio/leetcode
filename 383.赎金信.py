#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for i in magazine:
            if d.get(i):
                d[i] += 1
            else:
                d[i] = 1
        for j in ransomNote:
            if d.get(j):
                d[j] -= 1
            else:
                return False
        return True
# @lc code=end

