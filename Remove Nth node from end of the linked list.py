'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''
#solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
            
        if count == n:
            return head.next
        diff = count - n
        i = 1
        temp = head
        while i <=diff:
            if i < diff:
                temp = temp.next
            else:
                temp.next = temp.next.next
            i += 1
                
        return head
                