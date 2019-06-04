# TO-DO: complete the helper function below to merge 2 sorted arrays
# Merge each pair of individual element (which is by default, sorted) into sorted arrays of 2 elements,
# Merge each pair of sorted arrays of 2 elements into sorted arrays of 4 elements,
# Repeat the process...,
# Final step: Merge 2 sorted arrays of N/2 elements (for simplicity of this discussion,
#  we assume that N is even) to obtain a fully sorted array of N elements.


def merge(arrA, arrB):
    sorted = []
    while len(arrA) and len(arrB):
        if arrA[0] <= arrB[0]:
            sorted.append(arrA.pop(0))
        else:
            sorted.append(arrB.pop(0))
    results = [*sorted, *arrA, *arrB]
    return results


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    arr1 = arr[:len(arr)//2]
    arr2 = arr[len(arr)//2:]
    return merge(merge_sort(arr1), merge_sort(arr2))


# Algorithm
# ```
# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled
# ```
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
