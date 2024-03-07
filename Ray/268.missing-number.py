#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumofRe = n*(n+1)//2
        sumofinput = sum(nums)
        return sumofRe-sumofinput
        
# @lc code=end

