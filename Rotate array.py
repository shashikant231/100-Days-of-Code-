def rotate(nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        print(nums)
        while j <k:
            last = nums[len(nums)-1]
            nums[len(nums)-1] = 0
            for i in range(len(nums)-2,-1,-1):
                print(i)
                nums[i+1] = nums[i]

            nums[0] = last
            j +=1
        print(nums)

#Using recursion
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        def rightRotation(nums):
            last = nums[len(nums)-1]
            for i in range(len(nums)-2,-1,-1):
                nums[i+1] = nums[i]
            nums[0] = last
                
        for i in range(k):
            rightRotation(nums)
        return nums

rotate([1,2,3,4,5,6,7],3)