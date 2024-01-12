#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        num = [len(i) for i in strs ]
        tmp = strs[num.index(min(num))]
        flag = 0
        ans = ""
        for i in range(min(num)):
            for inst in strs:
                if inst[i] !=tmp[i]:
                    flag  = 1
                    break
            if flag != 1:
                ans+=tmp[i] 
        return ans
# @lc code=end

