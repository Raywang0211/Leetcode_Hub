#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        upper = len(nums)-1

        while low<=upper:
            mid = (upper+low)//2
            if nums[mid]<target:
                low = mid+1
                mid = mid+1
            elif nums[mid]>target:
                upper = mid-1
            else:
                return mid
        
        if mid<0:
            mid=0
        return mid
# @lc code=end

