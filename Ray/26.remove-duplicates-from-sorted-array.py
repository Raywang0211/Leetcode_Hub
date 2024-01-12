#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1,p2 = 0,1
        while p2<len(nums):
            if nums[p1]!=nums[p2]:
                p1+=1
                nums[p1] = nums[p2]
            p2+=1
        return p1+1
                  
# @lc code=end

