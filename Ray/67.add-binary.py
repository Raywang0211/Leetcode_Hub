#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a = a[::-1]
        b = b[::-1]
        ans = ""
        inc = 0
        total = max(len(a),len(b))
        if len(a)!= total:
            for i in range(total-len(a)):
                a=a+"0"
        if len(b)!= total:
            for i in range(total-len(b)):
                b=b+"0"
        
        for i in range(total):
            tmp = int(a[i])+int(b[i])+inc
            if tmp == 0:
                ans +="0"
                inc = 0
            elif tmp == 1:
                ans += "1"
                inc = 0
            elif tmp == 2:
                ans += "0"
                inc = 1
            elif tmp == 3:
                ans+="1"
                inc = 1
        if inc!=0:
            ans+="1"

        return ans[::-1]




        # @lc code=end

