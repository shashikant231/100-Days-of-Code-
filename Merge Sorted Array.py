'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

'''
#Time complexity O(n2)
# copy the elements and use insertion sort 
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2.copy()
        for i in range(1,m+n):
            j = i
            while j > 0 and nums1[j] < nums1[j-1]:
                nums1[j] ,nums1[j-1] = nums1[j-1],nums1[j]
                j -= 1
        nums1

#2nd solution,using merge sort function ,which merge to sorted array


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = k = 0
        n1 = nums1[:m]
        while i < m and j < n:
            if n1[i] >= nums2[j]:
                nums1[k] = nums2[j]
                j += 1
            else:
                nums1[k] = n1[i]
                i += 1
            k += 1
            
        while i < m:
            
            nums1[k] = n1[i]
            i+=1
            k+=1

        while j < n:
            nums1[k] = nums2[j]
            j+=1
            k+=1