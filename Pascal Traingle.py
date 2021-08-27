'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
solution
We are first creating an 2D array .our array after creation for rows = 5 will look like follows:
[[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]
we will iterate through each rows and according to the position of "i" pointer ,we will put values.
'''
#non recursive solution
def generate(numRows):
    arr = []
    for i in range(numRows):
        col = []
        for j in range(i+1):
            col.append(0)
        arr.append(col)
    for line in range(0,numRows):
        for i in range(0,line+1):
            if i == 0 or i == line:
                arr[line][i] = 1
            else:
                arr[line][i] = arr[line-1][i-1] + arr[line-1][i]
    return arr