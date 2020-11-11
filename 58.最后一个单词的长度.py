#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        lastwordlen = 0
        while n >1:
            if s[n-1] != ' ' :
                lastwordlen+=1
            if s[n-1] == ' ' and lastwordlen>0:
                break
        
        return lastwordlen

# @lc code=end

