'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''
#solution
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        return (" ".join(i[::-1] for i in s))
            