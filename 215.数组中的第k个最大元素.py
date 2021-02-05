#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
# from typing import List

# from random import randint
# class Solutions:
#     def findKthLargest(self,nums:List[int],k: int) -> int:
#         def helper(l,r):
#             idx = randint(l,r)
#             j,v = l,nums[idx]
#             nums[l],nums[idx] = nums[idx],nums[l]
#             for i in range(l,r+1):
#                 if nums[i] > v:
#                     j += 1
#                     nums[j],nums[i] = nums[i],nums[j]
#             nums[j],nums[l] = nums[l],nums[j]
#             return j

#         n = len(nums)
#         l,r = 0,n-1
#         k -= 1
#         while True:
#             t = helper(l,r)
#             if t == k: return nums[t]
#             elif t > k: r = t - 1
#             else: l = t+1
#         return -1

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def shift_up(new_idx):
            new_val = minheap[new_idx]
            while new_idx > 0 and minheap[(new_idx-1)//2]>new_val:
                minheap[new_idx] = minheap[(new_idx-1)//2]
                new_idx =(new_idx-1)//2
            minheap[new_idx] = new_val
            
        def shift_down(start,end):
            start_val = minheap(start)
            while start*2 +1 <=end:
                child = start*2+1
                if child+1<end and minheap[child]>minheap[child+1]:
                    child += 1
                if minheap[child] < start_val:
                    minheap[start] = minheap[child]
                    start = child
                else:
                    break
            minheap[start] = start_val
    
        minheap = []
        for i in range(min(len(nums),k)):
            minheap.append(nums[i])
            shift_up(i)
        
        for num in nums[k:]:
            if num > minheap[0]:
                minheap[0] = num
                shift_down(0,k-1)
        return minheap[0]


# @lc code=end

