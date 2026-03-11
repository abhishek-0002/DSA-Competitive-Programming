'''
You are given a string s consisting only lowercase alphabets and an integer k. 
Your task is to find the length of the longest substring that contains exactly k distinct 
characters.

Note : If no such substring exists, return -1. 

Examples:

Input: s = "aabacbebebe", k = 3
Output: 7
Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", 
which includes 'c', 'b', and 'e'.
Input: s = "aaaa", k = 2
Output: -1
Explanation: There's no substring with 2 distinct characters.

Intuition:
Classic sliding window problem with hashmap
Have a two pointers i,j where i iterates on all elements move i when frequency count > k
so we shrink the window size from left. Iterate j so we add elements by moving pointer j
count frequency of elements  if it crosses more than k shrink the window size from left 
'''

def longestKSubstr(self, s, k):
    # code here
    i, j = 0, 0
    freqCnt ={}
    maxlen = -1
    if k == 0 or len(s) == 0:
        return -1  # change to 0 if you prefer: return 0

    for j in range(len(s)):
        freqCnt[s[j]] = freqCnt.get(s[j],0) + 1
        while len(freqCnt) > k:
            freqCnt[s[i]] -= 1
            if freqCnt[s[i]] == 0:
                del freqCnt[s[i]]
            i += 1
        if len(freqCnt) == k:
            maxlen = max(maxlen,j-i+1)
    return maxlen