'''
Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
solution
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table = {}
        for i in magazine:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        for i in ransomNote:
            if i in table and table[i] > 0:
                table[i] -= 1
            else:
                return False
        return True