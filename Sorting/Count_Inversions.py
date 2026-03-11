'''
Given an array of integers arr[]. You have to find the Inversion Count of the array. 
Note : Inversion count is the number of pairs of elements (i, j) 
such that i < j and arr[i] > arr[j].

Examples:

Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

Input: arr[] = [2, 3, 4, 5, 6]
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count.
Input: arr[] = [10, 10, 10]
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.

Intuition:
condition 1: i< j
condition 2: left[i] > right[j]

Brute Froce!!!!
In this we have i, j loop j where j=i+1 and increment i after j reaches arr length
count inversions if arr[i]>arr[j]
But this has time complexity of o(n^2)

Another method!!!
Lets think if we can able to keep track of the elements of which the condition 1,2 already satisfies.
So first if we sort the array then we may easily skip nested loops, but the issue is the sorting
should not disturb the indecies.
One way is merge sort where we divide and conquer.
Array is divided into two halves left and right 
Then we again keep dividing the array then we check the condition
of 
if arr[i] < arr[j] :
Add the element arr[i] to result array
increment i
else:
Add the arr[j] to result and increment j
here we need to count the inversions
One main point is that if arr[i] > arr[j]
then arr[i+1], arr[i+2], ..... > arr[j]
so its count inversions = len(left) - i --> this will give the elements of left array


When Do You Think of Merge Sort?
1. Counting pairs
    Count inversions
    Count reverse pairs
    Count smaller elements after self

2. Relative ordering
    “How far from sorted?”
    “Number of elements greater/smaller on right”

3. Comparing two groups efficiently
    Something like:
        Instead of checking every pair, can I compare sorted halves?
'''
class Solution:
    def inversionCount(self, arr):
        def merge_sort(arr):
            # Code Here
            if len(arr) <=1:
                return arr,0
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            
            leftSorted, inv_left = merge_sort(left)
            rightSorted, inv_right = merge_sort(right)
            
            merged, inv_merged = merge(leftSorted,rightSorted)
            
            return merged, inv_left + inv_right + inv_merged
    
        def merge(left,right):
            i = 0
            j = 0
            result = []
            inv_count = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    inv_count += (len(left) - i)
                    j += 1
                
            result.extend(left[i:])
            result.extend(right[j:])
            
            return result, inv_count
        
        _, total = merge_sort(arr)
        return total