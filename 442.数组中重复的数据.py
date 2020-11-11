#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        rst = []
        for num in nums:
            index = abs(num) -1
            val = nums[index]
            if val < 0:
                rst.append(abs(num))
            nums[index] = -nums[index]
        return rst
# @lc code=end

