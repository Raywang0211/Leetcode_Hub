#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        ans = []
        for i in range(length-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            L = i+1
            R = length-1
            while L<R:
                total = nums[i]+nums[L]+nums[R]

                if total>0:
                    R-=1
                elif total<0:
                    L+=1
                else:
                    ans.append([nums[i],nums[L],nums[R]])
                    while L<R and nums[L]== nums[L+1]:
                        L+=1
                    while L<R and nums[R] == nums[R-1]:
                        R-=1
                    L+=1
                    R-=1
        return ans   
                
# @lc code=end

