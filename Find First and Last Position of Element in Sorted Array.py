'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

#solution
In the problem statement,it is mention that we have to find solution in 0(logn) time,which means we have to perform binary search.
In each case we will create left ,right and pos variables and start with left = 0 ,right = len(arr)-1 and pos = -1.if we find our target value in given array ,we will update the pos value to its index.
'''
class Solution:
    def searchRange(self, nums, target):
        #if array is empty
        if not nums:
            return [-1, -1]
        
        #binary search for first element
        left ,right , pos = 0,len(nums)-1,-1
        output = []
        while left <= right:
            mid = int(left+(right+1))//2
            if nums[mid] == target:
                pos = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        output.append(pos)
                
        #binary search for last element
        left ,right , pos = 0,len(nums)-1,-1
        while left <= right:
            mid = int(left+(right+1))//2
            if nums[mid] == target:
                pos = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        output.append(pos)
                
        return output