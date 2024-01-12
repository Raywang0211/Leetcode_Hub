#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        right_sign = ")]}"
        left_ = []

        for element in s:
            if element in right_sign:

                if not left_ or (
                    (element==")" and left_[-1]!="(") or
                    (element=="]" and left_[-1]!="[") or
                    (element=="}" and  left_[-1]!="{") 
                
                ):
                    return False
                left_.pop()
            else:
                left_.append(element)
        return not left_

        
# @lc code=end

