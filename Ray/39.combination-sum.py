#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        sig = []
        def helper(can,n,sig,pt):
            if n==0:
                ans.append(sig[:])
                return
            elif n<0:
                return
            
            for i in range(pt,len(can)):
                sig.append(can[i])
                helper(can, n-can[i], sig, i)
                sig.pop()
                
        helper(candidates,target,sig,0)
        return ans
# @lc code=end

