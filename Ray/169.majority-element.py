#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        total = {}
        max_number = len(nums)//2+1
        for i in nums:
            if str(i) in total:
                total[str(i)]+=1
                if total[str(i)]>=max_number:
                    return i
            else:
                total[str(i)]=1
                if total[str(i)]>=max_number:
                    return i
    
# @lc code=end

