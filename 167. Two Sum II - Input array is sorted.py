'''
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''
#use binary search technique

def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        if numbers[left] + numbers[right] == target:
            return ([left,right])
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1

print(twoSum([2,7,11,15],9))