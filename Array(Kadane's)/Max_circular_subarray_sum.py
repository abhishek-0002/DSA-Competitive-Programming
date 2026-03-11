'''
You are given a circular array arr[] of integers, find the maximum possible sum of a 
non-empty subarray. In a circular array, the subarray can start at the 
end and wrap around to the beginning. Return the maximum non-empty subarray sum, 
considering both non-wrapping and wrapping cases.

Examples:

Input: arr[] = [8, -8, 9, -9, 10, -11, 12]
Output: 22
Explanation: Starting from the last element of the array, i.e, 12, 
and moving in a circular fashion, we have max subarray as 12, 8, -8, 9, -9, 10, 
which gives maximum sum as 22.
Input: arr[] = [10, -3, -4, 7, 6, 5, -4, -1]
Output: 23
Explanation: Maximum sum of the circular subarray is 23. The subarray is 
[7, 6, 5, -4, -1, 10].
Input: arr[] = [5, -2, 3, 4]
Output: 12
Explanation: The circular subarray [3, 4, 5] gives the maximum sum of 12.



Intuition:
1. Kadane's algorithm

What does a circular subarray really mean?
In a circular array:

[ a  b  c  d  e ]

A wrapping subarray looks like:

[ d  e  a  b ]

otice something important:

👉 A wrapping subarray is the whole array
👉 except for some middle part that we exclude.

In this example, we excluded [ c ].

To maximize the wrapping sum:

We should exclude the smallest possible subarray.

Why?

Because:

max_circular = total_sum − excluded_part

If excluded_part is very small (very negative),
then subtracting it makes result very large.

So the best excluded part = minimum subarray sum.

Therefore:

max_circular = total_sum − min_subarray_sum
'''

class Solution:
    def maxCircularSum(self, arr):
        # code here
        curr_max = arr[0]
        max_sum = arr[0]
        min_sum = arr[0]
        curr_min = arr[0]
        total_sum = arr[0]
        n = len(arr)
        
        for i in range(1,n):
            curr_max = max(arr[i], curr_max+arr[i])
            max_sum = max(max_sum,curr_max)
            
            curr_min = min(arr[i],curr_min+arr[i])
            min_sum = min(min_sum, curr_min)
            
            total_sum += arr[i]
        
        if max_sum < 0:
            return max_sum
            
        
        return max(max_sum, total_sum - min_sum)