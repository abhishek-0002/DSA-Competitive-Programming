'''
Given an array arr[] consisting of positive integers, your task is to find the length of 
the longest subarray that contains at most two distinct integers.

Examples:

Input: arr[] = [2, 1, 2]
Output: 3
Explanation: The entire array [2, 1, 2] contains at most two distinct integers (2 and 1). 
Hence, the length of the longest subarray is 3.
Input: arr[] = [3, 1, 2, 2, 2, 2]
Output: 5
Explanation: The longest subarray containing at most two distinct integers 
is [1, 2, 2, 2, 2], which has a length of 5.

Intuition:

Sliding window problem
Whenever you see:

Longest / Maximum length subarray

With condition on distinct elements

Contiguous elements

👉 Think: Sliding Window (Two Pointers)
i → left pointer
j → right pointer
freqMap → stores element frequency
'''
class Solution:
    def totalElements(self, arr):
        # Code here
        Maxlen = 0
        freqMap = {}
        i = 0
        j = 0
        for j in range(len(arr)):
            freqMap[arr[j]] = freqMap.get(arr[j], 0) + 1
            while len(freqMap) > 2:
                freqMap[arr[i]] -= 1
                if freqMap[arr[i]] == 0:
                    del freqMap[arr[i]]
                i += 1   
            Maxlen = max(Maxlen,j-i+1)
        return Maxlen 