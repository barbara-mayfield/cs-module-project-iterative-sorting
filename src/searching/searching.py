def linear_search(arr, target):
    # Your code here
    for num in range(len(arr)):
        if arr[num] == target:
            return num
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = (len(arr) - 1)
    found = False

    while start <= end and not found:
        # get the middle index
        mid = (start + end) // 2

        # compare the value in the middle with target
        # if the middle is the same as target, set found to true
        if arr[mid] == target:
            return mid
        # move start or end index closer to one another, and shrink our search space
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1  # not found
