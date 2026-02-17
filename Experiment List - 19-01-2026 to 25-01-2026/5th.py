# Given an array arr[]. The task is to find the largest element and return it.
def largest(arr):
    max_element = arr[0]
    
    for num in arr:
        if num > max_element:
            max_element = num
            
    return max_element
