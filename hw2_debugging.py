"""hello welcome to ncsu"""

import rand


def merge_sort(arr: list[int]) -> list[int]:
    """Merge sort"""
    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr: list[int], right_arr: list[int]) -> list[int]:
    """Recombine"""
    left_index = 0
    right_index = 0
    merged_arr = [0] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merged_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merged_arr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        merged_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merged_arr[left_index + right_index] = left_arr[i]

    return merged_arr


xtemp = rand.random_array([0] * 20)
xfinal = merge_sort(xtemp)

print(xfinal)
# pyright: strict
