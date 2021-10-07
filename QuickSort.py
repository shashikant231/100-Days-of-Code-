def quicksort(array):
    quicksorthelper(array,0,len(array)-1)
    print(array)
def quicksorthelper(array,startIdx,endIdx):
    if startIdx >= endIdx:
        return 
    pivotIdx = startIdx
    leftIdx = startIdx+1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            array[leftIdx],array[rightIdx] = array[rightIdx],array[leftIdx]
        if array[leftIdx] < array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] > array[pivotIdx]:
            rightIdx -= 1
            
    array[rightIdx],array[pivotIdx] = array[pivotIdx],array[rightIdx]
    leftSubarrayisSmaller  = (rightIdx-1) - startIdx < endIdx
    if leftSubarrayisSmaller:
        quicksorthelper(array,startIdx,rightIdx-1)
        quicksorthelper(array,rightIdx+1,endIdx)
    else:
        quicksorthelper(array,rightIdx+1,endIdx)
        quicksorthelper(array,startIdx,rightIdx-1)

quicksort([9,1,45,67,34,5])