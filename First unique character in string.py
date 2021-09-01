'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
Example 1:
Input: s = "leetcode"
Output: 0
Example 2:
Input: s = "loveleetcode"
Output: 2
Example 3:
Input: s = "aabb"
Output: -1
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = {}
        for i in s:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        
        for key,value in table.items():
            if value == 1:
                return s.find(key)
            
            
        return -1
            