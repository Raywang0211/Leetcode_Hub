#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pt1,pt2 = 0,0
        k = 0
        re = 0
        while pt2<len(nums):
            if  nums[pt2]==val:
                pt2+=1
                re+=1
            else:
                k+=1
                nums[pt1] = nums[pt2]
                pt1+=1
                pt2+=1
            
        for i in range(re):
            nums.pop()
        return k
# @lc code=end

