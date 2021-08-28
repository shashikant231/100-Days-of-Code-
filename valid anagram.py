'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

solution
Create an array of length 256 ,and intialize it with 0.
First iterate through the string "s" and increament the value of count,then iterate through the string "t"
 and decreament the value ,if ord value of characters matches with count index .
'''
#count chracters
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count  = [0] * 256
        for i in s:
            count[ord(i)] += 1
            
        for i in t:
            count[ord(i)] -= 1
            
        for i in range(256):
            if count[i] != 0:
                return False
        return True

#hash table
def isAnagram(s,t):
    # if len(s) != len(t):
    #         return False
    table = {}
    for i in s:
        if i in table:
            table[i] += 1
        else:
            table[i] = 1

    for i in t:
        if i in table:
            table[i] -= 1
        else:
            return "false"

    for i in s:
        if table[i] != 0:
            return "false"
    return "true"


print(isAnagram("mat","tam"))

