import rand


def mergeSort(arr : list[int]) -> list[int]:
    if (len(arr) == 1):
        return arr

    half = len(arr) // 2

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))


def recombine(leftArr: list[int], rightArr: list[int]) -> list[int]:
    leftIndex = 0
    rightIndex = 0
    mergeArr = [0] * (len(leftArr) + len(rightArr))
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            rightIndex += 1
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        else:
            leftIndex += 1
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]

    for i in range(rightIndex, len(rightArr)):
        mergeArr[leftIndex + rightIndex] = rightArr[i]

    for i in range(leftIndex, len(leftArr)):
        mergeArr[leftIndex + rightIndex] = leftArr[i]

    return mergeArr


arr = rand.random_array([0] * 20)
arr_out = mergeSort(arr)

print(arr_out)
#pyright: strict
