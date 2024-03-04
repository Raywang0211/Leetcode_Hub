#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums,start,end):
            if start>end:
                return None
            mid = (start+end)//2
            node = TreeNode(nums[mid])
            node.left = helper(nums,start,mid-1)
            node.right = helper(nums,mid+1,end)
            return node
        
        return helper(nums,0,len(nums)-1)

        
# @lc code=end

