#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def isTree(root_left,root_right):
            if not root_left and not root_right:
                return True
            if not root_left or not root_right:
                return False
            if root_left.val == root_right.val:
                return True
            return all(isTree(root_left.left,root_right.right),isTree(root_left.right,root_right.left))
        return isTree(root,root)

# @lc code=end

