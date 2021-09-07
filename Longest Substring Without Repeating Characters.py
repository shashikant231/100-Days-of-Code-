'''
Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_idx = {}
        max_length = 0
        
        start_idx = 0
        for i in range(0,len(s)):
            if s[i] in last_idx:
                start_idx = max(start_idx,last_idx[s[i]]+1)
                
            max_length = max(max_length,i-start_idx+1)
            
            last_idx[s[i]] = i
            
        return max_length