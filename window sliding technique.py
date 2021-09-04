'''
Given an array of integers of size ‘n’.
Our aim is to calculate the maximum sum of ‘k’ 
consecutive elements in the array.

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4 
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23}
of size 4.

Input  : arr[] = {2, 3}
         k = 3
Output : Invalid
There is no subarray of size 3 as size of whole
array is 2.
'''
#brute force approach
#T = O(n*n)

def max_sum(arr,k):
    max_sum = -99999
    for i in range(len(arr)-k):
        sum = 0
        for j in range(i,i+k):
            sum = sum + arr[j]
        max_sum = max(sum,max_sum)

    return max_sum



#Solution using window sliding approch(optimal solution)
#T = O(n)

def max_sum(arr,k):
    sum = 0
    max_sum = -99999
    for i in range(k):
        sum = sum + arr[i]

    max_sum  = max(sum,max_sum)
    for j in range(k,len(arr)):
        sum = sum + arr[j] - arr[j-k]
        max_sum = max(sum,max_sum)

    print(max_sum)

max_sum([1, 4, 2, 10, 23, 3, 1, 0, 20],4)

    

    

