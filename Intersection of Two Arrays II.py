'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

'''

class Solution:
    def intersect(self, nums1, nums2):
        table = {}
        result = []
        for i in nums1:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        for i in nums2:
            if i in table:
                if table[i] > 1:
                    table[i] -= 1
                else:
                    del table[i]
                result.append(i)
        return result
        