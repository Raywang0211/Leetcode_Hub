#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def digsum(n):
            
            tmp = 0
            while n!=0:
                d = n%10
                tmp +=d*d
                n = n//10
            return tmp

        f = n
        s = n
        while 1:
            for i in range(2):
                f = digsum(f)
            s = digsum(s)
            if f==s:
                break
        
        if f==1:
            return True
        else:
            return False
        
# @lc code=end

