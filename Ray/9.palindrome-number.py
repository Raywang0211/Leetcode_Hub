#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        bake = x[::-1]
        if bake == x:
            return True
        else:
            return False
# @lc code=end

