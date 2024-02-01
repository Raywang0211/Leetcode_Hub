#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        digits = digits[::-1]
        for index,element in enumerate(digits):
            number+=(10**index)*element
        number = number+1
        
        output = []
        for i in str(number):
            output.append(int(i))

        return output

    

# @lc code=end

