#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n = 0
        for c in s:
            n ^= ord(c)
        for c in t:
            n ^= ord(c)
        return chr(n)
# @lc code=end

