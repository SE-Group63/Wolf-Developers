# """hello welcome to ncsu"""

import rand

def mergeSort(arr):
    if len(arr) <= 1:  # Base case: If array has 1 or no element, it's already sorted
        return arr

    half = len(arr) // 2
    # Recursively split the array into halves and merge them back together
    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))

def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = []

    # Merge the two arrays by comparing elements one by one
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr.append(leftArr[leftIndex])
            leftIndex += 1
        else:
            mergeArr.append(rightArr[rightIndex])
            rightIndex += 1

    # Append any remaining elements from the left or right array
    mergeArr.extend(leftArr[leftIndex:])
    mergeArr.extend(rightArr[rightIndex:])

    return mergeArr

xtemp = rand.random_array([0] * 20)
#xtemp = [23, 11, 8, 5, 8, 10, 11, 9, 23]
xfinal = mergeSort(xtemp)

print(xfinal)
# # pyright: strict
