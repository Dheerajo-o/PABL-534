# Given an array arr[]. Your task is to find the minimum and maximum elements
# in the array.
# Examples:
# Input: arr[] = [1, 4, 3, 5, 8, 6]
# Output: [1, 8]
# Explanation: minimum and maximum elements of array are 1 and 8.
class Solution:
    def getMinMax(self, arr):
        min_val = arr[0]
        max_val = arr[0]
        for i in arr:
            if i < min_val:
                min_val = i
            if i > max_val:
                max_val = i
        return min_val, max_val
