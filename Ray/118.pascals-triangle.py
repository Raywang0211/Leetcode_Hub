#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans =[]
        
        for i in range(numRows):
            tmp = [1]
            if i==0:
                ans.append(tmp)
            elif i==1:
                tmp.append(1)
                ans.append(tmp)
            elif i>=2:
                pre = ans[i-1]
                for j in range((len(ans[i-1])-1)):
                    new_n = ans[i-1][j]+ans[i-1][j+1]
                    tmp.append(new_n)
                tmp.append(1)
                ans.append(tmp)
        return ans 
# @lc code=end

