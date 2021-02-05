#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.  
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        cur,stack,res = root,[],[]
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            tmp = stack.pop()
            res.append(tmp.val)
            cur = tmp.right
        return res
# @lc code=end

