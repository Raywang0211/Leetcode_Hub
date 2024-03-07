#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid = len(nums)//2
        elem = set(nums)

        for i in elem:
            if nums.count(i)>mid:
                return i
    
# @lc code=end

