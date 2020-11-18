#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        p0 = 0
        p2 = n-1
        while i <= p2:
            while i < p2 and nums[p2] == 2:
                    p2 -= 1
            if nums[i] == 2:
                nums[p2],nums[i] = nums[i],nums[p2]
                p2 -=1
            if nums[i] == 0:
                nums[p0],nums[i] = nums[i],nums[p0]
                p0 += 1
            i += 1
        return nums
# @lc code=end

