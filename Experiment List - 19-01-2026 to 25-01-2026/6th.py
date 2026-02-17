# Given an array arr, rotate the array by one position in clockwise direction.
# Examples:
# Input: arr[] = [1, 2, 3, 4, 5]
# Output: [5, 1, 2, 3, 4]
# Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.
def rotate(arr):
    n = len(arr)
    if n == 0:
        return arr
    last = arr[-1]  
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last
    return arr
