#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def findmin(head,tail):
            fast = head
            slow = head
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def re_roor(head,tail):
            if head == tail: return None
            mid = findmin(head,tail)

            root = TreeNode(mid.val)
            root.left = re_roor(head,mid)
            root.right = re_roor(mid.next,tail)
            return root
            
        return re_roor(head,None)
# @lc code=end

