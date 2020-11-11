#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        res = ""
        count = 0
        list_s = list(S)

        while list_s:
            s = list_s.pop()
            if s != "-":
                if count % K == 0 and res != '':
                    res += '-'
                res += s.upper()
                count += 1
        return res[::-1]
        
# @lc code=end

