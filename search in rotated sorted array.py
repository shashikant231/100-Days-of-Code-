'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:
Input: nums = [1], target = 0
Output: -1


#solution
The logic of this problem can be summarised in three lines:

Find the pivot index,where rotation happens using binary search .For eg: in [4,5,6,7,0,1,2] pivot index is 4 .
Perform binary search on element starting from 0th index upto (pivot-1) index.
And again binary search on remaining element ,i.e from pivot index upto last index
Below is the implementation:
'''
class Solution:
    def search(self, nums, target):
        #fing the pivot index ,where rotation happens
        left,right ,last_element= 0,len(nums)-1,nums[-1]
        while left <= right:
            mid  =int(left+right)//2
            if last_element < nums[mid]:
                left = mid+1
            elif last_element >= nums[mid]:
                right = mid -1
                
        k = left
        #binary search on element before pivot index
        left ,right , pos = 0,k-1,-1
        while left <= right:
            mid = int(left+(right+1))//2
            if nums[mid] == target:
                pos = mid
                return pos
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
          
        #binary search on element after pivot index including pivot element
        left ,right , pos = k,len(nums)-1,-1
        while left <= right:
            mid = int(left+(right+1))//2
            if nums[mid] == target:
                pos = mid
                return pos
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        #executed when target is not in array 
        return pos