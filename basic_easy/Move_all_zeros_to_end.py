'''
You are given an array arr[] of non-negative integers. You have to move all the zeros in the 
array to the right end while maintaining the relative order of the non-zero elements. 
The operation must be performed in place, meaning you should not use extra space for 
another array.

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.

Intuition:
The problem can be solved with help of two arrays
But the space complexity will be O(n)

The problem can be solved via two pointer method 
take i, j = 0 starting of the array
Iterate i through the array if i points to non-zero element swap arr[i] with arr[j]
after swap move the j to next element.

So what we are doing?
we are trying to move non zero elements to the front of the array 
'''
def pushZerosToEnd(self, arr):
    	# code here
    j = 0
    for i in range(len(arr)):
    	if arr[i] != 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1