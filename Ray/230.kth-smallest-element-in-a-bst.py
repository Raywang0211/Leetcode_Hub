#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def helper(node):
            nonlocal ans,k
            if not node:
                return None
            helper(node.left)
            ans.append(node.val)
            k-=1
            if k==0:
                return
            helper(node.right)
        
        helper(root)
        return ans[k-1]
# @lc code=end

