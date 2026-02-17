#  You are given an integer array arr[]. You need to find the maximum sum of a 
# subarray (containing at least one element) in the array arr[]. 
# Note : A subarray is a continuous part of an array. 
# Examples: 
# Input: arr[] = [2, 3, -8, 7, -1, 2, 3] 
# Output: 11 
# Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.
class Solution:
    def maxSubArraySum(self,arr):
        max_current = arr[0]
        max_global = arr[0]  
        for i in range(1, len(arr)):
            max_current = max(arr[i], max_current + arr[i])
            max_global = max(max_global, max_current)
        return max_global
