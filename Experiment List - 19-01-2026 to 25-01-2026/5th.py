# Given an array arr[]. The task is to find the largest element and return it.
# Examples:
# Input: arr[] = [1, 8, 7, 56, 90]
# Output: 90
# Explanation: The largest element of the given array is 90.
# Input: arr[] = [5, 5, 5, 5]
def largest(arr):
    max_element = arr[0]
    
    for num in arr:
        if num > max_element:
            max_element = num
            
    return max_element
