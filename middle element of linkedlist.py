'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one


'''
#solution 1:raverse the whole linked list and count the no. of nodes.
#Now traverse the list again till count/2 and return the node at count/2. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        temp = head
        listnode_len = 1
        while temp.next != None:
            listnode_len += 1
            temp = temp.next
            
        mid = listnode_len // 2 + 1
        mid_elements = []
        temp = head
        count = 1
        i = 1
        if listnode_len == 1:
            return head
        while i <= mid:
            count += 1
            if count < mid:
                temp = temp.next
            elif count == mid:
                temp = temp.next
                return temp
                
            i += 1

#using two pointer approch
class Solution:
    def middleNode(self, head):
        bunnie = head
        tortoise = head
        while bunnie and bunnie.next:
            tortoise = tortoise.next
            bunnie = bunnie.next.next
            
        return tortoise
            

