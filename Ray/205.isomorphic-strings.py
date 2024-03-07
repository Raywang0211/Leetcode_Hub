#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        def check(s1,s2):
            dic = {}
            for i in range(len(s1)):
                if s1[i] not in dic:
                    dic[s1[i]] = s2[i]
                elif dic[s1[i]] != s2[i]:
                    return False
            return True
        
        return check(s,t) and check(t,s)

        
                
                
# @lc code=end

