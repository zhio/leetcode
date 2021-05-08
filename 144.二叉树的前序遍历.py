#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root : return []
        stack,res = [root],[]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return res
        
    def preorderTraversal2(self,root: TreeNode) -> List[int]:
        if not root: return []
        cur,res,stack = root,[],[]
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            tmp = stack.pop()
            cur = tmp.right
        return res
    
    def inorderTraversal2(self,root: TreeNode) -> List[int]:
        if not root: return []
        cur,stack,res = root,[],[]
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            tmp = stack.pop()
            res.append(tmp.val)
            cur = tmp.right
        return res
    
    def postorderTraversal(self,root: TreeNode) -> List[int]:
        if not root: return []
        cur, stack, res = root, [],[]
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            tmp = stack.pop()
            cur = tmp.left
        return res[::-1]
            
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack, res = [(0,root)],[]
        while stack:
            flag,node = stack.pop()
            if not node: continue
            if flag ==1:
                res.append(node.val)
            else:
                stack.append((1,node))
                stack.append((0,node.right))
                stack.append((0,node.left))
        return res

# @lc code=end

