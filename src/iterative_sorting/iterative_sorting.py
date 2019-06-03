# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # Algorithm
    # 1. Start with current index = 0

    # 2. For all indices EXCEPT the last index:

    #     a. Loop through elements on right-hand-side
    #     of current index and find the smallest element

    #     b. Swap the element at current index with the
    #     smallest element found in above loop
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        length = len(arr) - 1
        # 4 3
        while length > cur_index:
            if arr[length] < arr[smallest_index]:
                smallest_index = length
            length -= 1
        tmp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = tmp
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # TO-DO: swap
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)
    while n is not 1:
        for i in range(0, len(arr) - 1):
            curr = arr[i]  # 5
            next = arr[i + 1]  # 4
            if curr > next:
                arr[i] = next
                arr[i + 1] = curr
        n -= 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
