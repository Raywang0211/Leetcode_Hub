#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        ans = []
        for i in range(rowIndex+1):
            tmp = [1]
            if i == 0:
                ans.append(tmp)
                
            elif i==1:
                tmp.append(1)
                ans.append(tmp)
            else:
                for j in range(i-1):
                    tmp.append(ans[i-1][j]+ans[i-1][j+1])
                tmp.append(1)
                ans.append(tmp)
        return tmp
                
        
# @lc code=end

