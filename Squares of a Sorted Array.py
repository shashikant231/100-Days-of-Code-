''''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100]
'''
# Divide the array into two halves,positive and negative and store there squares into two lists
# At this point we have two sorted list ,we can easily merge the two sorted list
def sortedSquares(nums):
        pos = []
        neg = []
        result = []
        for i in nums:
            if i >= 0:
                pos.append(i * i)
            else:
                neg.append(i*i)
        neg = neg[: : -1]
        if len(neg) == 0:
            return pos
        i=j=k=0
        while i < len(pos) and j < len(neg):
            if pos[i] <= neg[j]:
                result.append(pos[i])
                i += 1
            else:
                result.append(neg[j])
                j += 1
            k += 1
        while i < len(pos):
            result.append(pos[i])
            k += 1
            i += 1
        while j < len(neg):
            result.append(neg[j])
            k += 1
            j += 1
        print(result)

sortedSquares([-4,-1,0,3,10])