"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        
        new_num = 0

        while x:
            if x>0:
                mod = x%10
                new_num = (new_num*10) + mod
                x=int(x/10)
                
                if new_num > int(2**31-1):
                    return 0

            else:
                mod = x%-10
                new_num = (new_num*10) + mod
                x=int(x/10)
                
                if new_num < int(-2**31):
                    return 0
                
        return new_num