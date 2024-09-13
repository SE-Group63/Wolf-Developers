import pytest
from hw2_debugging import mergeSort

def test_merge_sort_random():
    arr = [23, 11, 8, 5, 8, 10, 11, 9, 23]
    expected = [5, 8, 8, 9, 10, 11, 11, 23, 23]
    assert mergeSort(arr) == expected               # Test case 1: Unsorted array with random elements

def test_merge_sort_sorted():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert mergeSort(arr) == expected               # Test case 2: Already sorted array

def test_merge_sort_duplicates():
    arr = [4, 4, 4, 2, 2, 1, 1]
    expected = [1, 1, 2, 2, 4, 4, 4]
    assert mergeSort(arr) == expected               # Test case 3: Array with duplicate elements

def test_merge_sort_alternate():
    arr = [2, 1, 4, 3, 6, 5, 8, 7]
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    assert mergeSort(arr) == expected               # Test case 3: Array where alternate elements are not sorted

