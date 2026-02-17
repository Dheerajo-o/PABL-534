# Given an integer array arr[] and an integer k, your task is to find and return the kth smallest 
# element in the given array. 
# Note: The kth smallest element is determined based on the sorted order of the array. 
 
# Examples: 
 
# Input: arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4 
# Output: 5 
# Explanation: 4th smallest element in the given array is 5. 
# Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3 
# Output: 7 
# Explanation: 3rd smallest element in the given array is 7. 
# Constraints: 
# 1 ≤ arr.size() ≤ 105 
# 1 ≤ arr[i] ≤ 105 
# 1 ≤ k ≤  arr.size()
class Solution:
    def kthSmallest(self, arr, k):
        
        def partition(left, right):
            pivot = arr[right]
            i = left
            
            for j in range(left, right):
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            
            arr[i], arr[right] = arr[right], arr[i]
            return i
        
        def quickSelect(left, right):
            if left <= right:
                pivot_index = partition(left, right)
                
                if pivot_index == k - 1:
                    return arr[pivot_index]
                elif pivot_index > k - 1:
                    return quickSelect(left, pivot_index - 1)
                else:
                    return quickSelect(pivot_index + 1, right)
        
        return quickSelect(0, len(arr) - 1)
