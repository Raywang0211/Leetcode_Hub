#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_split = s.split(" ")
        while True:
            tmp = s_split.pop()
            if tmp!="":
                return len(tmp) 
    
        
# @lc code=end

