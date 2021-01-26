"""

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        minLength = len(strs[0])
        
        for i in range(len(strs)):
            minLength = min(len(strs[i]), minLength)
            
        lcp = ''
        i = 0
        
        while i < minLength:
            char = strs[0][i]
            
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return lcp
            
            lcp += char
                    
            i += 1
        return lcp
            
        
        
                
        
                
            
                
            
            