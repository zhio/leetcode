#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return 
        pre = ListNode(0)
        pre.next = head
        las = head
        cur = head
        while cur:
            if las.val <= cur.val:
                las = las.next
            else:
                tmp = pre
                while tmp.next.val <= cur.val:
                    tmp = tmp.val
                las.next = cur.next
                cur.next = tmp.next
                tmp.next = cur
            cur = las.next
        return pre.next
                
# @lc code=end

