#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def backtrack(s,l,r):
            if len(s) == 2*n:
                ans.append(s)
                return
            if l>r:
                backtrack(s+")",l,r+1)
            if l<n:
                backtrack(s+"(",l+1,r)

        backtrack("",0,0)
        return ans
        
# @lc code=end

