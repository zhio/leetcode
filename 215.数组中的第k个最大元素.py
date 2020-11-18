#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def helper(l,r):
            idx = randint(l,r)
            j,v = l,nums[idx]
            nums[l],nums[idx] = nums[idx],nums[l]
            for i in range(l,r+1):
                if nums[i] > v:
                    j += 1
                    nums[j],nums[i] = nums[i],nums[j]
            nums[j],nums[l] = nums[l],nums[j]
            return j
        n = len(nums)
        l,r = 0, n-1
        k -= 1
        while True:
            t = helper(l,r)
            if t == k: return nums[t]
            elif t > k:r = t-1
            else: l = t+1
            
        return -1
# @lc code=end

